from django.urls import path

from geofazendas.sindicatos.views import artigo, base


app_name = 'sindicatos'


urlpatterns = [
    path('', base.index, name='index'),
    path('minhas-publicacoes/', artigo.artigo_list, name='article_list'),
    path('minhas-publicacoes/nova/', artigo.artigo_create, name='article_create'),
    path('minhas-publicacoes/<int:pk>/editar/', artigo.artigo_update, name='article_update'),
    path('minhas-publicacoes/<int:pk>/remover/', artigo.artigo_delete, name='article_delete'),
]
