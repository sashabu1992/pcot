from django.shortcuts import render
from .models import ZagranTour, GalleryTour
# Create your views here.

def ZagranTourViews(request):

    return render(
        request,
        'pages/zagrantour.html',
        context={}
    )

def TourDetailCountry(request, slug_tourmaline):
    post = ZagranTour.objects.get(slug=slug_tourmaline, is_draft=True)
    tour = ZagranTour.objects.get(slug=slug_tourmaline)
    gallery = GalleryTour.objects.filter(tour=tour)
    return render(
        request,
        'pages/zagrantour_detail.html',
        context={'post': post, 'gallery':gallery}
    )