from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^/$', view_blog, name='blog_home'),
    url(r'^/(?P<blog_slug>.*)', single_blog, name='single_blog'),
]