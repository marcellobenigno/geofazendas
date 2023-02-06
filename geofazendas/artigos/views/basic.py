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
            tipo_artigo=self.tipo_artigo, data_publicacao__isnull=False
        )
        categoria = self.request.GET.get('categoria')
        if categoria:
            categoria = get_object_or_404(Categoria, slug=categoria)
            queryset = queryset.filter(category=categoria)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(text__icontains=q)
            )
        return queryset

    def latest_artigos(self):
        return Artigo.objects.filter(
            tipo_artigo=self.tipo_artigo, data_publicacao__isnull=False
        )[:3]

    def categories(self):
        return Categoria.objects.all()

    def tags(self):
        return Tag.objects.all()


class ArtigoDetailView(generic.DetailView):

    template_name = 'artigos/artigo_detail.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.visualizacoes += 1
        self.object.save()
        return response

    def get_queryset(self):
        return Artigo.objects.filter(data_publicacao__isnull=False)

    def tipo_artigo_url(self):
        if self.object.tipo_artigo == 'artigos':
            url_name = 'artigos:artigo_list'
        elif self.object.tipo_artigo == 'noticias':
            url_name = 'artigos:noticia_list'
        elif self.object.tipo_artigo == 'clima':
            url_name = 'artigos:clima_list'
        else:
            url_name = 'artigos:curso_list'
        return reverse(url_name)

    def latest_artigos(self):
        return Artigo.objects.filter(
            tipo_artigo=self.object.tipo_artigo, data_publicacao__isnull=False
        )[:3]

    def categories(self):
        return Categoria.objects.all()

    def tags(self):
        return Tag.objects.all()


artigo_list = ArtigoListView.as_view()
noticia_list = ArtigoListView.as_view(tipo_artigo='noticias')
curso_list = ArtigoListView.as_view(tipo_artigo='cursos')
clima_list = ArtigoListView.as_view(tipo_artigo='clima')
artigo_detail = ArtigoDetailView.as_view()
