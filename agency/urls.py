
from django.urls import path
from . import views

urlpatterns = [
    path('agency/', views.agency, name='agency'),
]