from django.contrib.gis.geos import GEOSGeometry
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from . import forms
from . import models
from .layers_list import lyr_list
from .serializers import EstadoSerializer, MunicipioSerializer, CarSerializer


class IndexView(generic.TemplateView):
    layer_list = lyr_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.PesquisaForm
        context['layers'] = self.layer_list
        return context


class GetDadosView(generic.TemplateView):
    template_name = 'mapas/dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        point = GEOSGeometry(f"POINT({kwargs['x']} {kwargs['y']})")
        context['municipio'] = models.MunicipioGeometria.objects.filter(geom__contains=point).first()
        context['assentamentos'] = models.Assentamento.objects.filter(geom__contains=point).first()
        context['area_indigena'] = models.AreaIndigena.objects.filter(geom__contains=point).first()
        context['area_protegida'] = models.AreaProtegida.objects.filter(geom__contains=point).first()
        context['imovel_venda'] = models.Car.objects.filter(anunciado=True, geom__contains=point).first()
        if kwargs['tema'] == 'solos':
            context['solo'] = models.Solo.objects.filter(geom__contains=point).first()
        if kwargs['tema'] == 'biomas':
            context['biomas'] = models.Bioma.objects.filter(geom__contains=point).first()
        if kwargs['tema'] == 'clima':
            context['clima'] = models.Clima.objects.filter(geom__contains=point).first()
        if kwargs['tema'] == 'declividade':
            context['declividade'] = models.Declividade.objects.filter(geom__contains=point).first()
        if kwargs['tema'] == 'geologia':
            context['geologia'] = models.Geologia.objects.filter(geom__contains=point).first()
        if kwargs['tema'] == 'geomorfologia':
            context['geomorfologia'] = models.Geomorfologia.objects.filter(geom__contains=point).first()
        if kwargs['tema'] == 'relevo':
            context['relevo'] = models.Relevo.objects.filter(geom__contains=point).first()
        if kwargs['tema'] == 'incidencia-solar':
            context['incidencia'] = models.Irradiacao.objects.filter(geom__contains=point).first()
        return context


class MobileView(generic.DetailView):
    template_name = 'mapas/mobile.html'

    def get_object(self, queryset=None):
        return models.Municipio.objects.get(
            pk=self.kwargs['municipio_id']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['municipio'] = self.get_object()
        return context


class EstadoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = models.Estado.objects.all()
    filterset_fields = ['id']
    pagination_class = None

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class MunicipioViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['estado']
    queryset = models.Municipio.objects.filter(visivel=True)
    serializer_class = MunicipioSerializer

    def paginate_queryset(self, queryset, view=None):
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    @action(methods=['GET'], detail=False)
    def por_ponto(self, request, pk=None):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        point = GEOSGeometry(f"POINT({longitude} {latitude})")
        municipio = models.Municipio.objects.filter(
            municipiogeometria__geom__contains=point
        ).first()
        if municipio:
            serializer = MunicipioSerializer(instance=municipio)
            return Response(data=serializer.data)
        return Response(status=404)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class CarViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cod_imovel']
    queryset = models.Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


class MunicipioAjax(generic.TemplateView):
    template_name = 'mapas/municipios.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['municipios'] = models.Municipio.objects.filter(
            estado_id=self.request.GET.get('estado_id')
        )
        return context


index = IndexView.as_view(template_name='mapas/index.html')
incidencia = IndexView.as_view(template_name='mapas/incidencia.html')
get_dados = GetDadosView.as_view()
mobile_view = MobileView.as_view()
municipio_ajax = MunicipioAjax.as_view()
