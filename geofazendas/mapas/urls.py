from django.urls import path

from geofazendas.mapas import views

app_name = 'mapas'

urlpatterns = [
    path('', views.index, name='index'),
    path('mobile/', views.mobile_view, name='mobile_view'),
    path('<path:x>/<path:y>/<str:tema>/', views.get_dados, name='get_dados'),
]
