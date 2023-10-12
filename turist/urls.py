from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns = [
      path('', views.TuristamViews, name='TuristamViews'),
      path('pdf/<slug:slug_turistampage>/', GeneratePdf.as_view() , name='CreatePdf'),
      path('<slug:slug_turistampage>/', views.DetailStrTuristam, name='DetailStrTuristam'),


]