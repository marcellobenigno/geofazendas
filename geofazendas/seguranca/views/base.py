from django.contrib.auth.views import LoginView as BaseLoginView

from geofazendas.seguranca.forms import LoginForm


class LoginView(BaseLoginView):

    form_class = LoginForm
    template_name = 'seguranca/login.html'


login = LoginView.as_view()
