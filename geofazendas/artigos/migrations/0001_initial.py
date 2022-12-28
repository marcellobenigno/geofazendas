# Generated by Django 4.1.3 on 2022-12-28 11:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(blank=True, default=True, verbose_name='Ativo')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Identificador')),
                ('ordem', models.PositiveSmallIntegerField(default=1, verbose_name='Ordem')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['ordem'],
            },
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(blank=True, default=True, verbose_name='Ativo')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Identificador')),
                ('tipo_artigo', models.CharField(choices=[('artigos', 'artigos'), ('noticias', 'noticias'), ('cursos', 'cursos')], max_length=20, verbose_name='Tipo do Artigo')),
                ('texto', ckeditor.fields.RichTextField(blank=True, verbose_name='Texto')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='articles/photos', verbose_name='Foto')),
                ('data_publicacao', models.DateField(blank=True, null=True, verbose_name='Data da publicação')),
                ('autor', models.CharField(blank=True, max_length=50, verbose_name='Autor')),
                ('visualizacoes', models.PositiveIntegerField(default=0, verbose_name='Visualizações')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artigos.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Artigo',
                'verbose_name_plural': 'Artigos',
                'ordering': ['-data_publicacao'],
            },
        ),
    ]
