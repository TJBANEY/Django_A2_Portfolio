from django.contrib import admin
from .models import BlogArticle

# Register your models here.

class BlogArticleAdmin(admin.ModelAdmin):
    model = BlogArticle
    list_display = ('title', 'posted', 'is_published')
    readonly_fields = ('is_published',)

admin.site.register(BlogArticle, BlogArticleAdmin)
