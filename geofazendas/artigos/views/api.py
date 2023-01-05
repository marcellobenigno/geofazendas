import datetime as dt

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action

from geofazendas.artigos.models import Artigo, Categoria
from geofazendas.artigos.serializers import CategoriaSerializer, ArtigoSerializer
from geofazendas.seguranca.permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Categoria.objects.filter(ativo=True)

    @action(methods=['GET'], detail=False, url_path='by-slug/(?P<slug>[-_\w]+)')
    def by_slug(self, request, *args, **kwargs):
        self.lookup_field = 'slug'
        return self.retrieve(request, *args, **kwargs)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArtigoSerializer
    queryset = Artigo.objects.filter(ativo=True)
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'category': ['exact'],
        'tipo_artigo': ['exact'],
        'tags': ['icontains']
    }

    def get_queryset(self):
        today = dt.datetime.now()
        return self.queryset.filter(data_publicacao__lte=today)

    @action(methods=['GET'], detail=False, url_path='by-slug/(?P<slug>[-_\w]+)')
    def by_slug(self, request, *args, **kwargs):
        self.lookup_field = 'slug'
        return self.retrieve(request, *args, **kwargs)
