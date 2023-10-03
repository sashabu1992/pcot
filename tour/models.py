from django.db import models
from slugify import slugify

from django.urls import reverse
import uuid
import os
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

CATEGORY_CHOISE = (
    ('kvartira', 'Квартиры'),
    ('komerch', 'Коммерческая недвижимость'),
    ('zagorod', 'Загородные дома'),
    ('garazh', 'Гаражи'),
    ('zemuch', 'Земельные участки'),
    ('newstroi', 'Новостройки'),
)


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
    post = CKEditor5Field(verbose_name="Содержание", blank=True, config_name='extends')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")

    """Основные характеристики"""
    best = models.BooleanField(default=False, verbose_name="Лучшее предложение")
    category = models.CharField(max_length=16, choices=CATEGORY_CHOISE, default='kvartira',
                                verbose_name="Тип отдыха")


    class Meta:
        ordering = ('title',)
        verbose_name = ('загрантуры')
        verbose_name_plural = ('загрантуры')

    def __str__(self):
        """Return title and username."""
        return str(self.h1)

    def get_absolute_url(self):
        return reverse('ZagranTourLink', kwargs={'slug_ZagranTourLink': self.slug})  # new

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.title)
        while ZagranTour.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = increment_slug(self.slug, self)
        super(ZagranTour, self).clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ZagranTour, self).save(*args, **kwargs)






