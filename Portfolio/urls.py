"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from .views import view_home

from rest_framework import routers
from api.views import BlogViewSet, CommentViewSet
from .models import Sitemap

sitemaps = {'blog': Sitemap}

router = routers.SimpleRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^$', view_home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls), name='api'),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
    url(r'^blog', include('blog.urls'))
]
