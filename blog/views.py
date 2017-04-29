import logging

from django.shortcuts import render

# Create your views here.
from blog.models import BlogArticle


def view_blog(request):
    blogs = BlogArticle.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def single_blog(request, blog_slug):
    slug = blog_slug.lstrip('/')

    try:
        blog = BlogArticle.objects.get(slug=slug)
    except Exception as e:
        logging.error(e)
        blog = None

    return render(request, 'single_blog.html', {'blog': blog})
