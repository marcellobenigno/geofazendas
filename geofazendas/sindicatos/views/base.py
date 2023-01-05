from django.views import generic

from geofazendas.artigos.models import Artigo

from taggit.models import Tag

from geofazendas.sindicatos.mixins import SindicatoRequiredMixin

class IndexView(SindicatoRequiredMixin, generic.TemplateView):

    template_name = 'sindicatos/index.html'

    def popular_artigos(self):
        return Artigo.objects.order_by('-views')

    def recent_artigos(self):
        return Artigo.objects.order_by('-data_publicacao')

    def tags(self):
        return Tag.objects.all()


index = IndexView.as_view()
