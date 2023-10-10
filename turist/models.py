from ckeditor.fields import RichTextField
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.


class ContentTourist(models.Model):
    language = models.CharField(max_length=16, unique=True, choices=settings.LANGUAGES, verbose_name=_('Язык'))
    # Контакты
    text_contact = RichTextField(config_name='awesome_ckeditor', verbose_name="Текст", blank=True)
    # Как купить тур online
    text_kak_kupit_tour = RichTextField(config_name='awesome_ckeditor', verbose_name="Текст", blank=True)
    # О НАС
    text_onas = RichTextField(config_name='awesome_ckeditor', verbose_name="Текст", blank=True)
    # Оплата
    text_oplata = RichTextField(config_name='awesome_ckeditor', verbose_name="Текст", blank=True)
    #Подарочные сертификаты
    text_podarok_sertificat = RichTextField(config_name='awesome_ckeditor', verbose_name="Текст", blank=True)
    #Скидки и акции
    text_skidki = RichTextField(config_name='awesome_ckeditor', verbose_name="Текст", blank=True)

    class Meta:
        verbose_name = _('Статический контент')
        verbose_name_plural = _('Статический контент')
        ordering = ['language']

    def __str__(self):
        """Return title and username."""
        return str(self.language)
