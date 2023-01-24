from django import forms

from . import models


class PesquisaForm(forms.Form):
    estado = forms.ModelChoiceField(
        queryset=models.Estado.objects.all(),
        label=None
    )
