from django.views import generic
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import get_object_or_404

from taggit.models import Tag

from geofazendas.artigos.models import Artigo, Categoria


class ArtigoListView(generic.ListView):

    template_name = 'artigos/index.html'
    tipo_artigo = 'artigos'
    paginate_by = 5

    def get_queryset(self):
        queryset = Artigo.objects.filter(
            tipo_artigo=self.tipo_artigo, publish_date__isnull=False
        )
        category = self.request.GET.get('categoria')
        if category:
            category = get_object_or_404(Categoria, slug=category)
            queryset = queryset.filter(category=category)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(text__icontains=q)
            )
        return queryset

    def latest_artigos(self):
        return Artigo.objects.filter(
            tipo_artigo=self.tipo_artigo, publish_date__isnull=False
        )[:3]

    def categories(self):
        return Categoria.objects.all()

    def tags(self):
        return Tag.objects.all()


class ArtigoDetailView(generic.DetailView):

    template_name = 'artigos/article_detail.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.views += 1
        self.object.save()
        return response

    def get_queryset(self):
        return Artigo.objects.filter(publish_date__isnull=False)

    def tipo_artigo_url(self):
        if self.object.tipo_artigo == 'artigos':
            url_name = 'artigos:artigo_list'
        elif self.object.tipo_artigo == 'noticias':
            url_name = 'artigos:noticias_list'
        else:
            url_name = 'artigos:cursos_list'
        return reverse(url_name)

    def latest_artigos(self):
        return Artigo.objects.filter(
            tipo_artigo=self.object.tipo_artigo, publish_date__isnull=False
        )[:3]

    def categories(self):
        return Categoria.objects.all()

    def tags(self):
        return Tag.objects.all()


artigo_list = ArtigoListView.as_view()
noticias_list = ArtigoListView.as_view(tipo_artigo='noticias')
cursos_list = ArtigoListView.as_view(tipo_artigo='cursos')
artigo_detail = ArtigoDetailView.as_view()
