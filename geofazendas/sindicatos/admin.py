from django.contrib import admin

from geofazendas.sindicatos.models import Sindicato


@admin.register(Sindicato)
class SindicatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'criado', 'modificado']
    search_fields = ['nome']
    filter_horizontal = ['municipios']
