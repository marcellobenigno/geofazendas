from django.urls import path
from django.contrib.auth.views import LogoutView

from geofazendas.seguranca.views import base


app_name = 'seguranca'


urlpatterns = [
    path('inicio/', base.inicio, name='inicio'),
    path('entrar/', base.login, name='login'),
    path('sair/', LogoutView.as_view(next_page='base:index'), name='logout'),
]
