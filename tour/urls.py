from django.urls import path
from . import views

urlpatterns = [
      path('', views.ZagranTourViews, name='ZagranTour'),
      path('zagrantury/<slug:slug_tourmaline>/', views.TourDetailCountry, name='TourDetailCountry'),

]