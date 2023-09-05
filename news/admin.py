from django.contrib import admin
# Register your models here.
# Register your models here.
from .models import News
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.safestring import mark_safe
from django import forms



@admin.register(News)
class News(admin.ModelAdmin):
    search_fields = ("h1", )
    list_display = ('h1', 'preview', 'created', 'is_draft', 'slug')
    fieldsets = (
    	('SEO', {
            'fields': ('title','description', 'slug')
        }),
        ('Содержимое', {
            'fields': ('h1', 'introtext','image_zast', 'post')
        }),
        ('Настройки', {
            'fields': ('category','created', 'modified', 'published_date', 'is_draft')
        }),

    )
    readonly_fields = ('created', 'modified', 'preview')
    list_filter = ('is_draft', 'category', )
    prepopulated_fields = {'slug': ('title',)}

    def preview(self, obj):
        if obj.image_zast:
            return mark_safe(f'<img style="max-width:100px" src="{obj.image_zast.url}">')
        else:
            return mark_safe('<img style="max-width:100px" src="/static/images/no-image.jpg">')




