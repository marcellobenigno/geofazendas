from django import forms

from geofazendas.artigos.models import Artigo


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        widgets = {
            'foto': forms.FileInput
        }
        fields = [
            'titulo',
            'categoria',
            'tipo_artigo',
            'texto',
            'foto',
            'data_publicacao',
            'autor',
            'tags',
        ]
