from django import forms

from ckeditor.widgets import CKEditorWidget

from geofazendas.artigos.models import Artigo


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        widgets = {
            'foto': forms.FileInput,
            'texto': CKEditorWidget,
        }
        fields = [
            'titulo',
            'categoria',
            'tipo_artigo',
            'resumo',
            'texto',
            'foto',
            'data_publicacao',
            'autor',
            'tags',
        ]
