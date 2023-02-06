from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import resolve_url

from rolepermissions.checkers import has_role

from geofazendas.seguranca.forms import LoginForm


class LoginView(BaseLoginView):

    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = 'seguranca/login.html'


class InicioView(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if has_role(self.request.user, 'anunciante'):
            return resolve_url('anuncios:inicio')
        elif has_role(self.request.user, 'sindicato'):
            return resolve_url('sindicatos:index')
        return resolve_url('base:index')


login = LoginView.as_view()
inicio = InicioView.as_view()
