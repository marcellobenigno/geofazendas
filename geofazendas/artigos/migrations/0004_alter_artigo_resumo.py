# Generated by Django 4.1.3 on 2023-02-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0003_artigo_resumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='resumo',
            field=models.TextField(default='', help_text='É exibido na listagem dos artigos, notícias e cursos', verbose_name='Resumo'),
        ),
    ]
