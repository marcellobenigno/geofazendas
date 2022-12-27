from django.urls import path

from geofazendas.base import views

app_name = 'base'


urlpatterns = [
    path('', views.index, name='index'),
]
