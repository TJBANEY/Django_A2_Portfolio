from django.http import HttpResponse
from django.shortcuts import render


def view_home(request):
    response = render(request, "index.html", {})

    response['Cache-Control'] = 'max-age=602000'

    return response
