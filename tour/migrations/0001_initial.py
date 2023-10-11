# Generated by Django 3.2.19 on 2023-10-10 12:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import tour.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZagranTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URl')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок Title')),
                ('description', models.CharField(blank=True, max_length=350, verbose_name='Описание Description')),
                ('h1', models.CharField(max_length=255, verbose_name='Заголовок H1')),
                ('post', ckeditor.fields.RichTextField()),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('is_draft', models.BooleanField(default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Загрантуры',
                'verbose_name_plural': 'Загрантуры',
                'ordering': ('title',),
            },
        ),

    ]