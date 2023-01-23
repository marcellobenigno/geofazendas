from django.views import generic

from taggit.models import Tag

from geofazendas.artigos.models import Artigo, Categoria

from geofazendas.mapas.layers_list import lyr_list


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['layers'] = lyr_list
        return context


class CreditoView(generic.TemplateView):
    template_name = 'credito.html'

    def latest_artigos(self):
        return Artigo.objects.filter(data_publicacao__isnull=False)[:3]

    def categories(self):
        return Categoria.objects.all()

    def tags(self):
        return Tag.objects.all()


class SuporteJuridico(CreditoView):
    template_name = 'suporte_juridico.html'


index = IndexView.as_view()
credito = CreditoView.as_view()
suporte_juridico = SuporteJuridico.as_view()
