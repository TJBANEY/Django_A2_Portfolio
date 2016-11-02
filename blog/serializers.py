from rest_framework import serializers
from . import models

class BlogArticleSerializer(serializers.Serializer):
    class Meta:
        fields = (
            'id',
            'title',
            'body',
            'slug',
            'category',
            'is_published'
        )
        model = models.BlogArticle

class CommentsSerializer(serializers.Serializer):
    class Meta:
        fields = (
            'id',
            'article',
            'subscriber',
            'text',
            'written_at'
        )
        model = models.Comment

class SubscriberSerializer(serializers.Serializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'photo',
            'joined'
        )
        model = models.Subscriber