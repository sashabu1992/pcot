from .models import ZagranTour


def get_zagran_tour_link(request):
    nav_link = ZagranTour.objects.filter(is_draft=True)
    return {'nav_link': nav_link}


# установка куки
