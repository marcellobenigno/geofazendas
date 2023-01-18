from django.views import generic

from rolepermissions.mixins import HasRoleMixin


class InicioView(HasRoleMixin, generic.TemplateView):

    template_name = 'anuncios/inicio.html'
    allowed_roles = ['anunciante']


inicio = InicioView.as_view()
