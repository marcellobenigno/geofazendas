from django.urls import path

from geofazendas.artigos.views import basic

app_name = 'artigos'


urlpatterns = [
    path('artigos/', basic.artigo_list, name='artigo_list'),
    path('noticias/', basic.noticia_list, name='noticia_list'),
    path('cursos/', basic.curso_list, name='curso_list'),
    path('clima/', basic.clima_list, name='clima_list'),
    path('<str:tipo_artigo>/<slug:slug>/', basic.artigo_detail, name='artigo_detail'),
]
