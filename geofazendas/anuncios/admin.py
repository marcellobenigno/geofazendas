from django.contrib import admin

from geofazendas.anuncios.models import (
    Anuncio, ArquivoAnuncio, Estrutura, OpcaoDiversos, TipoServico
)


@admin.register(Estrutura)
class EstruturaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ativo', 'criado', 'modificado']
    search_fields = ['nome']


@admin.register(OpcaoDiversos)
class OpcaoDiversosAdmin(admin.ModelAdmin):

    list_display = ['categoria', 'nome', 'ativo', 'criado', 'modificado']
    search_fields = ['nome']
    list_filter = ['categoria']


@admin.register(TipoServico)
class TipoServicoAdmin(admin.ModelAdmin):

    search_fields = ['nome']
    list_display = ['nome', 'criado', 'ativo', 'modificado']

class ArquivoAnuncioInline(admin.TabularInline):

    model = ArquivoAnuncio
    extra = 1


@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):

    list_display = ['nome', 'proprietario', 'ativo', 'criado', 'modificado']
    search_fields = ['nome', 'proprietario__nome', 'proprietario__email']
    filter_horizontal = ['estruturas']
    inlines = [ArquivoAnuncioInline]
