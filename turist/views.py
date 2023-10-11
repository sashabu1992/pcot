# Create your views here.
#

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContentTourist
from .process_pdf import html_to_pdf
from django.views.generic import View
from django.template.loader import render_to_string


def TuristamViews(request):
    return render(
        request,
        'pages/turistam_views.html',
        context={}
    )
def DetailStrTuristam(request, slug_turistampage):
    post = ContentTourist.objects.get(slug=slug_turistampage, is_draft=True)
    return render(
        request,
        'pages/turistam_views_detail.html',
        context={'post':post}
    )


# Creating a class based view
# Creating a class based view
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        data = ContentTourist.objects.all()
        open('templates/maket/pdf.html', "w" , encoding='utf-8').write(render_to_string('maket/result.html', {'data': data}))
        pdf = html_to_pdf('maket/pdf.html')
        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')