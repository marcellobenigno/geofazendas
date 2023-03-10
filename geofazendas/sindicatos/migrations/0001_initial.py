# Generated by Django 4.1.3 on 2023-01-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mapas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sindicato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(blank=True, default=True, verbose_name='Ativo')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Sindicato')),
                ('municipios', models.ManyToManyField(related_name='sindicatos', to='mapas.municipio', verbose_name='Municípios')),
            ],
            options={
                'verbose_name': 'Sindicato',
                'verbose_name_plural': 'Sindicatos',
                'ordering': ['nome'],
            },
        ),
    ]
