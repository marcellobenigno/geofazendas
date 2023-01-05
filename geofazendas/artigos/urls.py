from django.urls import path

from geofazendas.artigos.views import basic

app_name = 'artigos'


urlpatterns = [
    path('artigos/', basic.artigo_list, name='article_list'),
    path('noticias/', basic.noticias_list, name='news_list'),
    path('cursos/', basic.cursos_list, name='course_list'),
    path('<str:tipo_artigo>/<slug:slug>/', basic.artigo_detail, name='article_detail'),
]
