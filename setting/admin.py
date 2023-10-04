from django.contrib import admin
# Register your models here.
# Register your models here.
from .models import TuristamSettings, AgentamSettings, TourType


admin.site.register(TuristamSettings)
admin.site.register(AgentamSettings)
admin.site.register(TourType)


