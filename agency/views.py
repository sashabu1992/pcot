from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

def agency(request):
    return render(
        request,
        'pages/agentam.html',
        context={}
    )

