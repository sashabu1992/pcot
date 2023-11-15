from .models import TuristamSettings, AgentamSettings, WebsiteContent, BanerTurist, BanerAgent


def settings_data(request):
    settings_turist = TuristamSettings.objects.filter(language='ru').first()
    settings_agent = AgentamSettings.objects.filter(language='ru').first()
    settings_static = WebsiteContent.objects.filter(language='ru').first()
    baner_turist = BanerTurist.objects.all()
    baner_agent = BanerAgent.objects.all()
    url_get = request.get_full_path
    s = str(url_get)
    url_get = s[s.find("?") + 0:]
    url_get = "'".join(url_get.split("'")[:-1])
    return {'settings_turist': settings_turist, 'settings_agent': settings_agent, 'settings_static':settings_static,'baner_turist':baner_turist, 'baner_agent':baner_agent, 'url_get':url_get}

def cookies_set(request):
    if not request.COOKIES.get('cat_razdel'):
        cat_razdel = 'turist'
    else:
        cat_razdel = request.COOKIES['cat_razdel']
    return {'cat_razdel': cat_razdel }

# установка куки
