from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail


def glav(request):
    return render(
        request,
        'pages/index.html',
        context={}
    )

# установка куки
def setcookies(request):
    # получаем из строки запроса имя пользователя
    cat_razdel = request.GET.get("cat_razdel", "")
    # создаем объект ответа
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    # передаем его в куки
    response.set_cookie("cat_razdel", cat_razdel)
    return response