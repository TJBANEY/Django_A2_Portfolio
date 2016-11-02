from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', view_blog, name='blog_home')
]