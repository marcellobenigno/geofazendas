from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.permissions import SAFE_METHODS

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import EstadoSerializer, MunicipioSerializer
from .models import Estado, Municipio


class EstadoViewSet(viewsets.ModelViewSet):

    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class MunicipioViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado']
    queryset = Municipio.objects.filter(visible=True)
    serializer_class = MunicipioSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]
