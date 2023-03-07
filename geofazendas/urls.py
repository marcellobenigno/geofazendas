from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from geofazendas.artigos.views import api as artigos_views
from geofazendas.mapas import views as maps_views
from geofazendas.seguranca.views import api as security_api

router = DefaultRouter()
# security
router.register('seguranca/usuario', security_api.UsuarioViewSet, basename='usuario')
# artigos
router.register('artigos/categoria', artigos_views.CategoryViewSet, basename='categoria')
router.register('artigos/artigos', artigos_views.ArticleViewSet, basename='artigos')
# maps
router.register('mapas/estados', maps_views.EstadoViewSet, basename='estado')
router.register('mapas/municipios', maps_views.MunicipioViewSet, basename='municipio')
router.register('mapas/car', maps_views.CarViewSet, basename='car')
router.register('mapas/temas', maps_views.TemasView, basename='tema')

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('seguranca/', include('geofazendas.seguranca.urls', namespace='seguranca')),
    path('sindicatos/', include('geofazendas.sindicatos.urls', namespace='sindicatos')),
    path('anuncios/', include('geofazendas.anuncios.urls', namespace='anuncios')),
    path('api/login/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('mapas/', include('geofazendas.mapas.urls', namespace='mapas')),
    path('martor/', include('martor.urls')),
    path('', include('geofazendas.base.urls', namespace='base')),
    path('', include('geofazendas.artigos.urls', namespace='artigos')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
