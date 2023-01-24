from django.urls import path

from geofazendas.base import views

app_name = 'base'


urlpatterns = [
    path('', views.index, name='index'),
    path('credito/', views.credito, name='credito'),
    path('suporte-juridico/', views.suporte_juridico, name='suporte_juridico'),
]
