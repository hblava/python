#引入path
from django.urls import path

# 引入 views.py
from . import views

# 部署应用的名称
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/',views.article_list,name='article_list'),
]
