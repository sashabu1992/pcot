from django.contrib import admin
from .models import ZagranTour, GalleryTour
from django.utils.safestring import mark_safe
from django import forms

#Предпросмотр фото
class PostImageInlineForm(forms.ModelForm):
    def preview(self, obj):
        return mark_safe(f'<img style="max-width:100px" src="{obj.image.url}">')


class GalleryTour(admin.TabularInline):
    model = GalleryTour
    extra = 0

@admin.register(ZagranTour)
class ZagranTour(admin.ModelAdmin):
    search_fields = ("h1", )
    list_display = ('h1', 'created', 'is_draft', )
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
    inlines = [GalleryTour]
    readonly_fields = ('created', 'modified', 'preview')
    list_filter = ('is_draft',)
    prepopulated_fields = {'slug': ('title',)}

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:100px" src="{obj.image_zast.url}">')





