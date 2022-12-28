from django.contrib import admin

from .models import Artigo, Categoria


@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'criado', 'modificado']
    search_fields = ['titulo', 'slug']
    prepopulated_fields = {
        'slug': ['titulo']
    }


@admin.register(Artigo)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'slug', 'data_publicacao', 'criado_por', 'criado', 'modificado']
    search_fields = ['titulo', 'slug', 'texto']
    list_filter = ['tipo_artigo', 'categoria', 'data_publicacao']
    prepopulated_fields = {
        'slug': ['titulo']
    }
