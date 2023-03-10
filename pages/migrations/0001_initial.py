# Generated by Django 4.1.3 on 2022-11-23 01:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL Amigable')),
                ('order', models.IntegerField(default=0, verbose_name='Orden')),
                ('visible', models.BooleanField(default=False, verbose_name='¿Visible?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Publicado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima Actualización')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
                'db_table': 'tb_Page',
            },
        ),
    ]
