from django.http import HttpResponse
from django.shortcuts import render


def view_home(request):
    return render(request, 'index.html', {})
