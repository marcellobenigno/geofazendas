from django.contrib import admin

from .models import Artigo, Categoria

@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug', 'created', 'modified']
    search_fields = ['title', 'slug']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Artigo)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug', 'publish_date', 'author', 'created', 'modified']
    search_fields = ['title', 'slug', 'text']
    list_filter = ['article_type', 'category', 'publish_date']
    prepopulated_fields = {
        'slug': ['title']
    }
