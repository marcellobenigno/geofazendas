from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, UserManager as BaseUserManager, PermissionsMixin
)
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from geofazendas.base.models import BaseModel


class UsuarioManager(BaseUserManager):

    def _create_user(self, identificador, password, **extra_fields):
        """
        Create and save a user with the given cpf and password.
        """
        user = self.model(identificador=identificador, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, identificador=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(identificador, password, **extra_fields)

    def create_superuser(self, identificador, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(identificador, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin, BaseModel):

    identificador = models.CharField('Identificador', unique=True, max_length=50)
    nome = models.CharField('Nome', max_length=20)
    email = models.EmailField('E-mail', blank=True)
    # contact
    municipio = models.ForeignKey(
        'mapas.Municipio', models.SET_NULL, blank=True, null=True, verbose_name='Município'
    )
    sindicato = models.ForeignKey(
        'sindicatos.Sindicato', models.SET_NULL, blank=True, null=True, verbose_name='Sindicato'
    )
    telefone = models.CharField('Telefone', max_length=11, blank=True)
    # admin
    is_staff = models.BooleanField('Equipe', default=False)
    ultimo_acesso = models.DateTimeField('Último acesso', null=True, blank=True, editable=False)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-first_name']

    def __str__(self):
        return self.nome

    @property
    def is_active(self):
        return self.ativo

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return self.nome.split()[0]

    def uidb64(self):
        return urlsafe_base64_encode(force_bytes(self.pk))


class SMS(BaseModel):
    telefone = models.CharField('Celular', max_length=20)
    codigo = models.CharField('Código', max_length=6)

    def __str__(self):
        return f'{self.telefone}: {self.codigo}'

    class Meta:
        verbose_name = 'Envio SMS'
        verbose_name_plural = 'Envios SMS'
        ordering = ['-created']
