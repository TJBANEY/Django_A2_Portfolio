from django.shortcuts import get_object_or_404
# from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import mixins

# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response

from blog.models import BlogArticle, Subscriber, Comment
from blog.serializers import *

# class ListCreateBlog(APIView):
#     def get(self, request, format=None):
#         blogs = BlogArticle.objects.all()
#         serializer = BlogArticleSerializer(blogs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BlogArticleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ListCreateBlog(generics.ListCreateAPIView):
#     queryset = BlogArticle.objects.all()
#     serializer_class = BlogArticleSerializer
#
# class RetrieveUpdateDestroyBlog(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogArticle.objects.all()
#     serializer_class = BlogArticleSerializer
#
# class ListCreateComment(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentsSerializer
#
#     def get_queryset(self):
#         return self.queryset.filter(blog=self.kwargs.get('blog_pk'))
#
#     # Method thats run when object is being created by view
#     def perform_create(self, serializer):
#         blog = get_object_or_404(BlogArticle, pk=self.kwargs.get('blog_pk'))
#         serializer.save(blog=blog)
#
# class RetrieveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentsSerializer
#
#     def get_object(self):
#         return get_object_or_404(
#             self.get_queryset(),
#             blog=self.kwargs.get('blog_id'),
#             pk=self.kwargs.get('pk')
#         )

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogArticle.objects.all()
    serializer_class = BlogArticleSerializer

    @detail_route(methods=['get'])
    def comments(self, request, pk=None):
        blog = self.get_object()
        serializer = CommentsSerializer(blog.comments.all(), many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

# class ExampleMixinClass(mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     pass