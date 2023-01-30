from django.urls import path

from geofazendas.mapas import views

app_name = 'mapas'

urlpatterns = [
    path('', views.index, name='index'),
    path('2/', views.mapa_vue, name='mapa_vue'),
    path('mobile/<int:municipio_id>/', views.mobile_view, name='mobile_view'),
    path('<path:x>/<path:y>/<str:tema>/', views.get_dados, name='get_dados'),
    path('municipio-ajax/', views.municipio_ajax, name='municipio_ajax'),
    path('incidencia-solar/', views.incidencia, name='incidencia'),
]
