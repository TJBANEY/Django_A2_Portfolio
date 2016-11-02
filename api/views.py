from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import BlogArticle, Subscriber, Comment
from blog.serializers import *

class ListBlog(APIView):
    def get(self, request, format=None):
        blogs = BlogArticle.objects.all()
        serializer = BlogArticleSerializer(blogs, many=True)
        return Response(serializer.data)