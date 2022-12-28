import random

import requests
from django.conf import settings
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework.filters import CharFilter
from django_filters.rest_framework.filterset import FilterSet
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from geofazendas.seguranca.models import SMS, Usuario
from geofazendas.seguranca.serializers import (
    VerificarSMSSerializer, LoginSMSSerializer, UsuarioRegistroSerializer, UsuarioSerializer, PasswordChangeSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    class UsuarioFilterSet(FilterSet):

        busca = CharFilter(method='filter_busca')

        def filter_busca(self, queryset, name, value):
            if value:
                value = value.replace('.', '').replace('-', '')
                queryset = queryset.filter(
                    Q(first_name__icontains=value) | Q(last_name__icontains=value)
                )
            return queryset

        class Meta:
            model = Usuario
            fields = ['busca']

    filter_backends = (DjangoFilterBackend,)
    filter_class = UsuarioFilterSet

    def get_serializer_class(self):
        if self.action == 'create':
            return UsuarioRegistroSerializer
        elif self.action == 'login_sms':
            return LoginSMSSerializer
        elif self.action == 'check_sms':
            return VerificarSMSSerializer
        return UsuarioSerializer

    def get_permissions(self):
        if self.action in ['create', 'login_sms', 'options']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Usuario.objects.filter(Q(is_staff=False) | Q(pk=self.request.user.pk))
        return Usuario.objects.filter(pk=self.request.user.pk)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def login_sms(self, request, *args, **kwags):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(True)
        phone = serializer.validated_data['phone']
        user = Usuario.objects.filter(identifier=phone).first()
        if user:
            sms = SMS.objects.create(
                phone=f'{phone}', code=random.randint(100000, 999999)
            )
            url = 'https://api.mobizon.com.br/service/message/sendSmsMessage'
            params = {'output': 'json', 'api': 'v1', 'apiKey': settings.SMS_API_TOKEN}
            if not phone.startswith('+55'):
                phone = f'+55{phone}'
            payload = {
                'recipient': phone,
                'text': f'Código do GeoFazendas para o seu Acesso: {sms.code}'
            }
            headers = {
                'cache-control': 'no-cache'
            }
            r = requests.post(url, params=params, data=payload, headers=headers)
            return Response({'sucesso': True})
        return Response({'erro': 'Nenhum usuário encontrado'}, status=400)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def check_sms(self, request, *args, **kwags):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(True)
        phone = serializer.validated_data['phone']
        code = serializer.validated_data['code']
        user = Usuario.objects.filter(identifier=phone).first()
        sms = SMS.objects.filter(phone=phone, code=code).first()
        if user and sms:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'sucesso': True, 'token': token.key})
        return Response({'erro': 'Código inválido'}, status=400)

    @action(detail=False, methods=['GET', 'POST', 'PUT', 'PATCH'])
    def meus_dados(self, request, pk=None):
        status = 200
        if request.method in ['POST', 'PUT', 'PATCH']:
            if request.method == 'POST':
                serializer = UsuarioSerializer(request.user, data=request.data)
            else:
                serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
            serializer.is_valid(True)
            serializer.save()
            data = serializer.data
        else:
            serializer = UsuarioSerializer(request.user)
            data = serializer.data
        return Response(data=data, status=status)

    @action(detail=False, methods=['PUT'])
    def alterar_senha(self, request, pk=None):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(True)
        serializer.save()
        return Response({'success': True})
