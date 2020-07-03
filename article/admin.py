from django.contrib import admin

# Register your models here.
# 导入ArticlePost
from .models import ArticlePost

admin.site.register(ArticlePost)
