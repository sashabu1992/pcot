# importing the necessary libraries
import os
from io import BytesIO, StringIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.encoding import smart_str

from pcot import settings


def fetch_pdf_resources(uri, rel):
    if uri.find(settings.MEDIA_URL) != -1:
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    elif uri.find(settings.STATIC_URL) != -1:
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
    else:
        path = None
    return path


# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     html = smart_str(html, encoding='utf-8')
     result = BytesIO()
     pdf = pisa.CreatePDF(html.encode("UTF-8"), dest=result, encoding='UTF-8', link_callback=fetch_pdf_resources)

     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None