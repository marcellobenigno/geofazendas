import datetime as dt

from rest_framework import viewsets
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend

from geofazendas.seguranca.permissions import IsAdminOrReadOnly

from geofazendas.artigos.models import Artigo, Categoria
from geofazendas.artigos.serializers import CategoriaSerializer, ArtigoSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Categoria.objects.filter(active=True)

    @action(methods=['GET'], detail=False, url_path='by-slug/(?P<slug>[-_\w]+)')
    def by_slug(self, request, *args, **kwargs):
        self.lookup_field = 'slug'
        return self.retrieve(request, *args, **kwargs)


class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = ArtigoSerializer
    queryset = Artigo.objects.filter(active=True)
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'category': ['exact'],
        'article_type': ['exact'],
        'tags': ['icontains']
    }

    def get_queryset(self):
        today = dt.datetime.now()
        return self.queryset.filter(publish_date__lte=today)

    @action(methods=['GET'], detail=False, url_path='by-slug/(?P<slug>[-_\w]+)')
    def by_slug(self, request, *args, **kwargs):
        self.lookup_field = 'slug'
        return self.retrieve(request, *args, **kwargs)
