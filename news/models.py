from ckeditor.fields import RichTextField
from django.db import models
from slugify import slugify

from django.urls import reverse
import uuid
import os
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

CATEGORY_CHOISE = (
    ('agent', 'Новости агентам'),
    ('turist', 'Новости туристам'),

)


def get_file_image_zast(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/news_zast/', filename)


class News(models.Model):
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="URl")
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Заголовок Description", blank=True)

    """Основные данные """
    h1 = models.CharField(max_length=255, verbose_name="Заголовок H1")
    image_zast = models.ImageField(upload_to=get_file_image_zast, verbose_name="Заставка новости", blank=True)
    post = RichTextField(config_name='awesome_ckeditor')
    introtext = models.TextField(max_length=1000, verbose_name="Краткое описание", blank=True)
    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")

    """Категория новости"""
    category = models.CharField(max_length=16, choices=CATEGORY_CHOISE, default='turist', verbose_name="Категория новости")


    class Meta:
        ordering = ('title',)
        verbose_name = ('Новость')
        verbose_name_plural = ('Новости')

    def __str__(self):
        """Return title and username."""
        return str(self.h1)

    def get_absolute_url(self):
        return reverse('DetailNews', kwargs={'slug_news': self.slug})  # new

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

