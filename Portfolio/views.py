import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def view_home(request):
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=7)
    response = render(request, "index.html", {})

    response['Cache-Control'] = 'max-age=602000'
    response['Expires'] = expiry_date

    print(settings.STATIC_ROOT)

    return response
