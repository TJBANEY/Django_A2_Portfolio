from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^', ListBlog.as_view(), name='blog_list')
]