from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms

# Register your models here.
# Register your models here.
from .models import TuristamSettings, AgentamSettings, TourType, WebsiteContent, BanerTurist, BanerAgent


admin.site.register(TuristamSettings)
admin.site.register(AgentamSettings)
admin.site.register(TourType)
admin.site.register(WebsiteContent)




@admin.register(BanerTurist)
class BanerTurist(admin.ModelAdmin):
    list_display = ('id', 'preview', 'name','alt', 'url' )

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image.url}">')

@admin.register(BanerAgent)
class BanerAgent(admin.ModelAdmin):
    list_display = ('id', 'preview', 'name','alt', 'url' )

    def preview(self, obj):
        return mark_safe(f'<img style="max-width:200px" src="{obj.image.url}">')


