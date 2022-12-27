from django.contrib import admin

from geofazendas.sindicatos.models import Sindicato


@admin.register(Sindicato)
class SindicatoAdmin(admin.ModelAdmin):

    list_display = ['name', 'created', 'modified']
    search_fields = ['name']
    filter_horizontal = ['counties']
