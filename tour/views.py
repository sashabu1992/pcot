from django.shortcuts import render
from .models import ZagranTour
# Create your views here.

def ZagranTourViews(request):
    data = ZagranTour.objects.filter(is_draft=True)
    return render(
        request,
        'pages/zagrantour.html',
        context={'data': data}
    )

def TourDetailCountry(request, slug_tourmaline):
    post = ZagranTour.objects.get(slug=slug_tourmaline, is_draft=True)
    return render(
        request,
        'pages/zagrantour_detail.html',
        context={'post': post}
    )