from django.contrib import admin
from .models import ContentTourist
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import forms
from django.contrib import admin
# Register your models here.
# Register your models here.




@admin.register(ContentTourist)
class ContentTourist(admin.ModelAdmin):
    search_fields = ("h1", )
    list_display = ('h1', 'created', 'is_draft', 'slug')
    fieldsets = (
    	('SEO', {
            'fields': ('title','description', 'slug')
        }),
        ('Содержимое', {
            'fields': ('h1', 'post')
        }),
        ('Настройки', {
            'fields': ('created', 'modified', 'is_draft')
        }),

    )
    readonly_fields = ('created', 'modified', )
    list_filter = ('is_draft', )
    prepopulated_fields = {'slug': ('title',)}








#@admin.register(ContentTourist)
#class ContentTourist(admin.ModelAdmin):
#    list_display = ('language', )
#    fieldsets = (
#        ('Язык', {
#            'fields': ('language',)
#        }),
#        ('О НАС', {
#            'fields': ('text_onas',)
#        }),
#    )
#



