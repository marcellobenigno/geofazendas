from django.urls import path

from geofazendas.mapas import views

app_name = 'mapas'

urlpatterns = [
    path('', views.index, name='index'),
    path('mobile/<int:municipio_id>/', views.mobile_view, name='mobile_view'),
    path('<path:x>/<path:y>/<str:tema>/', views.get_dados, name='get_dados'),
    path('incidencia-solar/', views.incidencia, name='incidencia'),
    path('monitoramento/', views.monitoramento, name='monitoramento'),
    path('foco-queimadas-48hs/', views.focos_queimadas, name='focos_queimadas'),
]
