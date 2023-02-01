from django.urls import path

from geofazendas.base import views

app_name = 'base'


urlpatterns = [
    path('', views.index, name='index'),
    path('credito/', views.credito, name='credito'),
    path('suporte-juridico/', views.suporte_juridico, name='suporte_juridico'),
    path('privacidade/', views.privacidade, name='privacidade'),
    path('privacidade/politica-privacidade/', views.politica_privacidade, name='politica_privacidade'),
    path('privacidade/politica-cookies/', views.politica_cookies, name='politica_cookies'),
]
