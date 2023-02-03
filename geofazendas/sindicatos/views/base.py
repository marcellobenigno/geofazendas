from django.utils import timezone
from django.views import generic

from taggit.models import Tag

from geofazendas.artigos.models import Artigo

from geofazendas.sindicatos.mixins import SindicatoRequiredMixin

class IndexView(SindicatoRequiredMixin, generic.TemplateView):

    template_name = 'sindicatos/index.html'

    def artigos_populares(self):
        return Artigo.objects.order_by('-visualizacoes')

    def artigos_recentes(self):
        return Artigo.objects.order_by('-data_publicacao')

    def tags(self):
        return Tag.objects.all()

    def primeira_noticia(self):
        return self.noticias().first()

    def noticias(self):
        hoje = timezone.now()
        return Artigo.objects.filter(
            tipo_artigo='noticia', data_publicacao__gte=hoje, data_publicacao__isnull=False
        )

    def clima(self):
        hoje = timezone.now()
        return Artigo.objects.filter(
            tipo_artigo='clima', data_publicacao__gte=hoje, data_publicacao__isnull=False
        )

    def primeiro_clima(self):
        return self.clima().first()

    def cursos(self):
        hoje = timezone.now()
        return Artigo.objects.filter(
            tipo_artigo='curso', data_publicacao__gte=hoje, data_publicacao__isnull=False
        )

    def primeiro_curso(self):
        return self.cursos().first()


index = IndexView.as_view()
