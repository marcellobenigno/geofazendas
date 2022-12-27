from rest_framework import serializers

from django.utils.html import strip_tags

from .models import Artigo, Categoria


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = [
            'id',
            'titulo',
            'slug',
            'criado',
            'modificado',
        ]


class ArtigoSerializer(serializers.ModelSerializer):

    resumo = serializers.SerializerMethodField()
    categoria_titulo = serializers.SerializerMethodField()
    tags_list = serializers.SerializerMethodField()

    def get_resumo(self, obj):
        return strip_tags(obj.texto)[:100]

    def get_category_title(self, obj):
        if obj.categoria:
            return obj.categoria.titulo
        return ''

    def get_tags_list(self, obj):
        return [tag.strip() for tag in obj.tags.split(',')]

    class Meta:
        model = Artigo
        fields = [
            'id',
            'titulo',
            'slug',
            'categoria',
            'tipo_artigo',
            'resumo',
            'categoria_titulo',
            'texto',
            'autor',
            'tags',
            'tags_list',
            'criado',
            'modificado',
        ]
