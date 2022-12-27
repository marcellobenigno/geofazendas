from django.db import models

from geofazendas.base.models import BaseModel


class Sindicato(BaseModel):

    nome = models.CharField('Nome do Sindicato', max_length=50)
    municipios = models.ManyToManyField('mapas.Municipio', verbose_name='Municípios', related_name='sindicatos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sindicato'
        verbose_name_plural = 'Sindicatos'
        ordering = ['nome']
