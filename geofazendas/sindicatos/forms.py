from django import forms

from geofazendas.artigos.models import Artigo


class ArtigoForm(forms.ModelForm):

    class Meta:
        model = Artigo
        widgets = {
            'photo': forms.FileInput
        }
        fields = [
            'title',
            'category',
            'article_type',
            'text',
            'photo',
            'publish_date',
            'author',
            'tags',
        ]
