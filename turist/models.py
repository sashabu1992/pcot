from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from slugify import slugify
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.


#class ContentTourist(models.Model):
#    language = models.CharField(max_length=16, unique=True, choices=settings.LANGUAGES, verbose_name=_('Язык'))
#    # Контакты
#    text_contact = RichTextField(config_name='awesome_ckeditor', verbose_name="Текст", blank=True)
#    # Как купить тур online
#
#    class Meta:
#        verbose_name = _('Статический контент')
#        verbose_name_plural = _('Статический контент')
#        ordering = ['language']
#
#    def __str__(self):
#        """Return title and username."""
#        return str(self.language)




class ContentTourist(models.Model):
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="URl")
    """СЕО натсрйоки"""
    title = models.CharField(max_length=255, verbose_name="Заголовок Title")
    description = models.CharField(max_length=350, verbose_name="Заголовок Description", blank=True)

    """Основные данные """
    h1 = models.CharField(max_length=255, verbose_name="Заголовок H1")
    post = RichTextField(config_name='awesome_ckeditor')
    created = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")
    modified = models.DateField(auto_now=True, verbose_name="Дата изменения")
    is_draft = models.BooleanField(default=True, verbose_name="Опубликован")


    class Meta:
        ordering = ('title',)
        verbose_name = ('Страницы')
        verbose_name_plural = ('Страницы')

    def __str__(self):
        """Return title and username."""
        return str(self.h1)

    def get_absolute_url(self):
        return reverse('DetailStrTuristam', kwargs={'slug_turistampage': self.slug})  # new

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(ContentTourist, self).save(*args, **kwargs)