from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

class TuristamSettings(models.Model):
    language = models.CharField(max_length=16, unique=True, choices=settings.LANGUAGES, verbose_name=_('Язык'))
    # Контактные данные
    phone1 = models.CharField(max_length=25, blank=True, verbose_name=_('Основной телефон'))
    phone1_viber= models.BooleanField(default=False, verbose_name=_('Есть Viber'))
    phone1_teleg=models.BooleanField(default=False, verbose_name=_('Есть Telegram'))
    phone1_whatsapp=models.BooleanField(default=False, verbose_name=_('Есть WhatsApp'))
    phone2 = models.CharField(max_length=25, blank=True, verbose_name=_('Дополнительный телефон'))
    phone2_viber =models.BooleanField(default=False, verbose_name=_('Есть Viber'))
    phone2_teleg =models.BooleanField(default=False, verbose_name=_('Есть Telegram'))
    phone2_whatsapp =models.BooleanField(default=False, verbose_name=_('Есть WhatsApp'))
    email = models.CharField(max_length=200, blank=True, verbose_name=_('Email'))
    addr = models.TextField(max_length=500, blank=True, verbose_name=_('Адрес'))
    # Соцсети и мессенджеры:
    vk = models.CharField(max_length=1000, blank=True, verbose_name=_('Вконтакте'))
    teleg = models.CharField(max_length=1000, blank=True, verbose_name=_('Телеграм'))
    inst = models.CharField(max_length=1000, blank=True, verbose_name=_('Instagram'))
    facebook = models.CharField(max_length=1000, blank=True, verbose_name=_('Facebook'))
    twitter = models.CharField(max_length=1000, blank=True, verbose_name=_('Twitter'))
    okdnoklassniki = models.CharField(max_length=1000, blank=True, verbose_name=_('Одноклассники'))
    youtube = models.CharField(max_length=1000, blank=True, verbose_name=_('YouTube'))
    tiktok = models.CharField(max_length=1000, blank=True, verbose_name=_('TikTok'))

    class Meta:
        verbose_name = _('Настройки раздел "Туристам"')
        verbose_name_plural = _('Настройки раздел "Туристам"')
        ordering = ['language']

    def __str__(self):
        """Return title and username."""
        return str(self.language)

class AgentamSettings(models.Model):
    language = models.CharField(max_length=16, unique=True, choices=settings.LANGUAGES, verbose_name=_('Язык'))
    # Контактные данные
    phone1 = models.CharField(max_length=25, blank=True, verbose_name=_('Основной телефон'))
    phone1_viber = models.BooleanField(default=False, verbose_name=_('Есть Viber'))
    phone1_teleg = models.BooleanField(default=False, verbose_name=_('Есть Telegram'))
    phone1_whatsapp = models.BooleanField(default=False, verbose_name=_('Есть WhatsApp'))
    phone2 = models.CharField(max_length=25, blank=True, verbose_name=_('Дополнительный телефон'))
    phone2_viber = models.BooleanField(default=False, verbose_name=_('Есть Viber'))
    phone2_teleg = models.BooleanField(default=False, verbose_name=_('Есть Telegram'))
    phone2_whatsapp = models.BooleanField(default=False, verbose_name=_('Есть WhatsApp'))
    email = models.CharField(max_length=200, blank=True, verbose_name=_('Email'))
    addr = models.TextField(max_length=500, blank=True, verbose_name=_('Адрес'))
    # Соцсети и мессенджеры:
    vk = models.CharField(max_length=1000, blank=True, verbose_name=_('Вконтакте'))
    teleg = models.CharField(max_length=1000, blank=True, verbose_name=_('Телеграм'))
    inst = models.CharField(max_length=1000, blank=True, verbose_name=_('Instagram'))
    facebook = models.CharField(max_length=1000, blank=True, verbose_name=_('Facebook'))
    twitter = models.CharField(max_length=1000, blank=True, verbose_name=_('Twitter'))
    okdnoklassniki = models.CharField(max_length=1000, blank=True, verbose_name=_('Одноклассники'))
    youtube = models.CharField(max_length=1000, blank=True, verbose_name=_('YouTube'))
    tiktok = models.CharField(max_length=1000, blank=True, verbose_name=_('TikTok'))

    class Meta:
        verbose_name = _('Настройки раздел "Агенствам"')
        verbose_name_plural = _('Настройки раздел "Агенствам"')
        ordering = ['language']

    def __str__(self):
        """Return title and username."""
        return str(self.language)


class TourType(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name="Тип отдыха")
    class Meta:
        ordering = ('name',)
        verbose_name = ('Тип отдыха')
        verbose_name_plural = ('Тип отдыха')

    def __str__(self):
        """Return title and username."""
        return str(self.name)

class WebsiteContent(models.Model):
    language = models.CharField(max_length=16, unique=True, choices=settings.LANGUAGES, verbose_name=_('Язык'))
    text_politica = RichTextField(config_name='awesome_ckeditor')


    class Meta:
        verbose_name = _('Статический контент')
        verbose_name_plural = _('Статический контент')
        ordering = ['language']

    def __str__(self):
        """Return title and username."""
        return str(self.language)

