# Generated by Django 4.1.3 on 2023-01-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='resumo',
            field=models.TextField(blank=True, help_text='É exibido na listagem dos artigos, notícias e cursos', verbose_name='Resumo'),
        ),
    ]
