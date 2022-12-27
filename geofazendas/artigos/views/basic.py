from django.views import generic
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import get_object_or_404

from taggit.models import Tag

from geofazendas.artigos.models import Artigo, Categoria


class ArtigoListView(generic.ListView):

    template_name = 'articles/index.html'
    article_type = 'artigos'
    paginate_by = 5

    def get_queryset(self):
        queryset = Artigo.objects.filter(
            article_type=self.article_type, publish_date__isnull=False
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

    def latest_articles(self):
        return Artigo.objects.filter(
            article_type=self.article_type, publish_date__isnull=False
        )[:3]

    def categories(self):
        return Categoria.objects.all()

    def tags(self):
        return Tag.objects.all()


class ArtigoDetailView(generic.DetailView):

    template_name = 'articles/article_detail.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.views += 1
        self.object.save()
        return response

    def get_queryset(self):
        return Artigo.objects.filter(publish_date__isnull=False)

    def article_type_url(self):
        if self.object.article_type == 'artigos':
            url_name = 'artigos:artigo_list'
        elif self.object.article_type == 'noticias':
            url_name = 'artigos:noticias_list'
        else:
            url_name = 'artigos:cursos_list'
        return reverse(url_name)

    def latest_articles(self):
        return Artigo.objects.filter(
            article_type=self.object.article_type, publish_date__isnull=False
        )[:3]

    def categories(self):
        return Categoria.objects.all()

    def tags(self):
        return Tag.objects.all()


artigo_list = ArtigoListView.as_view()
noticias_list = ArtigoListView.as_view(article_type='noticias')
cursos_list = ArtigoListView.as_view(article_type='cursos')
artigo_detail = ArtigoDetailView.as_view()
