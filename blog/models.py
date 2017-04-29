from django.db import models

# Create your models here.
class Subscriber(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=200)
    email = models.EmailField()

    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
        ordering = ('username', 'joined')

class BlogArticle(models.Model):
    title = models.CharField(max_length=255)

    image = models.ImageField(null=True, blank=True, upload_to='media')
    body = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    category = models.ForeignKey
    is_published = models.BooleanField(default=False)

    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('posted',)

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class Tag(models.Model):
    title = models.CharField(max_length=255)

class Comment(models.Model):
    article = models.ForeignKey(BlogArticle)
    subscriber = models.ForeignKey(Subscriber)
    text = models.TextField()

    written_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subscriber.username + ' - ' + self.written_at + ' - ' + self.article.title

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('article', 'written_at')
