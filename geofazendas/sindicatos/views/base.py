from django.views import generic

from geofazendas.artigos.models import Artigo

from taggit.models import Tag

from geofazendas.sindicatos.mixins import SindicatoRequiredMixin

class IndexView(SindicatoRequiredMixin, generic.TemplateView):

    template_name = 'syndicates/index.html'

    def popular_articles(self):
        return Artigo.objects.order_by('-views')

    def recent_articles(self):
        return Artigo.objects.order_by('-publish_date')

    def tags(self):
        return Tag.objects.all()


index = IndexView.as_view()
