from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.db import models
from slugify import slugify

from django.urls import reverse
import uuid
import os
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


def increment_slug(slug, obj):
    """
    Добавляет числовой суффикс к slug, если он уже существует в базе данных.
    Например, если slug="test", а в базе данных уже есть запись с таким slug,
    то функция вернет "test-1". Если "test-1" тоже уже существует, то вернет "test-2" и т.д.
    """
    original_slug = slug
    counter = 1
    while ZagranTour.objects.filter(slug=slug).exclude(id=obj.id).exists():
        slug = '{}-{}'.format(original_slug, counter)
        counter += 1
    return slug if original_slug == slug else slug + '-1'



class ZagranTour(models.Model):
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="URl")
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Описание Description", blank=True)

    """Основные данные """
    h1 = models.CharField(max_length=255, verbose_name="Заголовок H1")
    post = RichTextField(config_name='awesome_ckeditor')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")



    class Meta:
        ordering = ('title',)
        verbose_name = ('Загрантуры')
        verbose_name_plural = ('Загрантуры')

    def __str__(self):
        """Return title and username."""
        return str(self.h1)

    @property
    def get_absolute_url(self):
        return reverse('TourDetailCountry', kwargs={'slug_tourmaline': self.slug})  # new

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)
        while ZagranTour.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = increment_slug(self.slug, self)
        super(ZagranTour, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ZagranTour, self).save(*args, **kwargs)


#popular = models.BooleanField(default=False, verbose_name="Популярный тур")
#tourType = models.ForeignKey('TourType', on_delete=models.PROTECT, blank=False, verbose_name="Тип отдыха")
# Тип отдыха







