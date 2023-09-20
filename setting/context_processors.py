from .models import TuristamSettings, AgentamSettings


def settings_data(request):
    settings_turist = TuristamSettings.objects.filter(language='ru').first()
    settings_agent = AgentamSettings.objects.filter(language='ru').first()
    url_get = request.get_full_path
    s = str(url_get)
    url_get = s[s.find("?") + 0:]
    url_get = "'".join(url_get.split("'")[:-1])
    return {'settings_turist': settings_turist, 'settings_agent': settings_agent, 'url_get':url_get}