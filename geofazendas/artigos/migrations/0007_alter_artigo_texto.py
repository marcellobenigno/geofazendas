# Generated by Django 4.1.3 on 2023-02-10 13:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0006_alter_artigo_tipo_artigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Texto'),
        ),
    ]
