from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

from geofazendas.base.models import BaseModel


class Categoria(BaseModel):
    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True)
    ordem = models.PositiveSmallIntegerField('Ordem', default=1)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['ordem']


class Artigo(BaseModel):
    ARTICLE_TYPE_CHOICES = (
        (v, v) for v in ('artigos', 'noticias', 'cursos')
    )

    titulo = models.CharField('Título', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True)
    categoria = models.ForeignKey(
        Categoria, models.SET_NULL, null=True, blank=True, verbose_name='Categoria'
    )
    tipo_artigo = models.CharField(
        'Tipo do Artigo', max_length=20, choices=ARTICLE_TYPE_CHOICES
    )
    texto = RichTextField(verbose_name='Texto', blank=True)
    foto = models.ImageField('Foto', upload_to='artigos/photos', null=True, blank=True)
    data_publicacao = models.DateField('Data da publicação', null=True, blank=True)
    autor = models.CharField('Autor', max_length=50, blank=True)
    tags = TaggableManager(verbose_name='Tags / Marcadores', blank=True)
    visualizacoes = models.PositiveIntegerField('Visualizações', default=0)
    criado_por = models.ForeignKey(
        'seguranca.Usuario', models.SET_NULL, null=True, blank=True, related_name='artigos'
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['-data_publicacao']


def pre_save_article(instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        i = 1
        while Artigo.objects.filter(slug=instance.slug).exists():
            instance.slug = f'{instance.slug}-{i}'


models.signals.pre_save.connect(pre_save_article, sender=Artigo, dispatch_uid='pre_save_article')
