from django.shortcuts import render

# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.shortcuts import render

# 导入数据模型 ArticlePost
from .models import ArticlePost

# 视图函数
def article_list(request):
    #return HttpResponse("Hello World!")
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    #需要传递给模板(templates)的对象
    context = { 'articles': articles}
    # render函数 载入模板 并返回context对象
    return render(request,'article/list.html',context)
