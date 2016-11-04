from django.conf.urls import url
from .views import *

# urlpatterns = [
#     url(r'^', ListCreateBlog.as_view(), name='blog_list'),
#     url(r'^(?P<pk>\d+)/$', RetrieveUpdateDestroyBlog.as_view(), name='blog_rud'),
#     url(r'^(?P<blog_pk>\d+)/comments/$',
#         ListCreateComment.as_view(),
#         name='comment_list'),
#     url(r'^(?P<blog_pk>\d+)/comments/(?P<pk>\d+)/$$',
#         RetrieveUpdateDestroyComment.as_view(),
#         name='comment_list')
# ]