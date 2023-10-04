import os
from django.core.files.storage import FileSystemStorage
from pcot import settings
from urllib.parse import urljoin
from datetime import datetime


def get_filename(filename, request):
    return filename.upper()