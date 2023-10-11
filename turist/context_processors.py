from .models import ContentTourist


def get_turistam_link(request):
    nav_link_turistam = ContentTourist.objects.filter(is_draft=True)
    return {'nav_link_turistam': nav_link_turistam}


