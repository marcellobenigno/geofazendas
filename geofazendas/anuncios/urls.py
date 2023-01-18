from django.urls import path

from geofazendas.anuncios.views import base


app_name = 'anuncios'


urlpatterns = [
    path('', base.inicio, name='inicio'),
]
