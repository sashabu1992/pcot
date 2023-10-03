from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

from django.http import HttpResponse

def glav(request):
    if not request.COOKIES.get('cat_razdel'):
        cat_razdel = 'turist'
    else:
        cat_razdel = request.COOKIES['cat_razdel']
    return render(
        request,
        'pages/index.html',
        context={ 'cat_razdel':cat_razdel}
    )

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    cat_razdel = request.GET.get("cat_razdel", "")
    # создаем объект ответа
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    # передаем его в куки
    response.set_cookie("cat_razdel", cat_razdel)
    return response