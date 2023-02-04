from django import forms

from martor.widgets import AdminMartorWidget

from geofazendas.artigos.models import Artigo


class ArtigoForm(forms.ModelForm):

    class Meta:
        model = Artigo
        fields = [
            'titulo',
            'slug',
            'categoria',
            'tipo_artigo',
            'resumo',
            'texto',
            'foto',
            'data_publicacao',
            'autor',
            'tags',
        ]
        widgets = {
            'texto': AdminMartorWidget
        }

