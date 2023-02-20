from django.views import generic
from django.shortcuts import redirect

from rolepermissions.checkers import has_role

from taggit.models import Tag

from geofazendas.artigos.models import Artigo, Categoria

from geofazendas.mapas.layers_list import lyr_list


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff and has_role(self.request.user, 'sindicato'):
            return redirect('sindicatos:index')
        return super().get(self, request, *args, **kwargs)

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


class SuporteJuridicoView(CreditoView):
    template_name = 'suporte_juridico.html'


class PrivacidadeView(generic.TemplateView):
    template_name = 'privacidade.html'


class PoliticaPrivacidadeView(generic.TemplateView):
    template_name = 'includes/politica_privacidade.html'


class PoliticaCookiesView(generic.TemplateView):
    template_name = 'includes/politica_cookies.html'


index = IndexView.as_view()
credito = CreditoView.as_view()
suporte_juridico = SuporteJuridicoView.as_view()
privacidade = PrivacidadeView.as_view()
politica_privacidade = PoliticaPrivacidadeView.as_view()
politica_cookies = PoliticaCookiesView.as_view()
