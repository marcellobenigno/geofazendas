from django.urls import path

from geofazendas.mapas import views

app_name = 'mapas'


urlpatterns = [
    path('', views.index, name='index'),
]