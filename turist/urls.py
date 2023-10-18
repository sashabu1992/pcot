from django.urls import path
from . import views
from .views import GeneratePdf, generate_doc

urlpatterns = [
      path('', views.TuristamViews, name='TuristamViews'),
      path('pdf/<slug:slug_turistampage>/', GeneratePdf.as_view() , name='CreatePdf'),
      path('generate-doc/<slug:slug_turistampage>/', generate_doc, name='generate_doc'),
      path('<slug:slug_turistampage>/', views.DetailStrTuristam, name='DetailStrTuristam'),


]