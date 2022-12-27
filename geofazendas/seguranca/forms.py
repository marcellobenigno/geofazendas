from django import forms
from django.contrib.auth import authenticate

from geofazendas.seguranca.models import Usuario


class LoginForm(forms.Form):

    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.user = None

    def get_user(self):
        return self.user

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user = authenticate(self.request, identifier=email, password=password)
            if not self.user:
                raise forms.ValidationError('E-mail ou senha inválidos!')
        return self.cleaned_data


class UserAdminForm(forms.ModelForm):

    new_password = forms.CharField(
        label='Nova Senha', widget=forms.PasswordInput,
        required=False,
        help_text='Informe uma senha caso deseje alterar, caso contrário deixa esse campo em branco'
    )

    def save(self, commit=True):
        new_password = self.cleaned_data.get('new_password', '')
        if new_password:
            self.instance.set_password(new_password)
        return super().save(commit=commit)

    class Meta:
        model = Usuario
        exclude = ['password']
