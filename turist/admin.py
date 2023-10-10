from django.contrib import admin

from .models import ContentTourist
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import forms


@admin.register(ContentTourist)
class ContentTourist(admin.ModelAdmin):
    list_display = ('language', )
    fieldsets = (
        ('Язык', {
            'fields': ('language',)
        }),
        ('О НАС', {
            'fields': ('text_onas',)
        }),
        ('Скидки и акции', {
            'fields': ('text_skidki',)
        }),
        ('Подарочные сертификаты', {
            'fields': ('text_podarok_sertificat',)
        }),
        ('Оплата', {
            'fields': ('text_oplata',)
        }),
        ('Как купить тур online', {
            'fields': ('text_kak_kupit_tour',)
        }),
        ('Контакты', {
            'fields': ('text_contact',)
        }),


    )




