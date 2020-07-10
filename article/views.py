from django.shortcuts import render

# Create your views here.

# 导入 HttpResponse 模块
from django.http import HttpResponse
from django.shortcuts import render

# 导入数据模型 ArticlePost
from .models import ArticlePost
import markdown

# 引入redirect重定向模块
from django.shortcuts import render,redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User


# 视图函数
def article_list(request):
    #return HttpResponse("Hello World!")
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    #需要传递给模板(templates)的对象
    context = { 'articles': articles}
    # render函数 载入模板 并返回context对象
    return render(request,'article/list.html',context)


# 文章详情
def article_detail(request,id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
 
   # 将markdown 语法渲染成html样式
    article.body = markdown.markdown(article.body,
    extensions=[
    # 包含 缩写 表格等常用扩展
    'markdown.extensions.extra',
    # 语法高亮扩展
    'markdown.extensions.codehilite',
    ])

    # 需要传递给模板的对象
    context = {'article': article }
    # 载入模板，并返回context对象
    return render(request,'article/detail.html',context)


# 写文章的视图
def article_create(request):
    #判断用户是否提交数据
    if request.method == 'POST':
        #将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form }
        # 返回模板
        return render(request,'article/create.html',context)


# 删文章
def article_delete(request,id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")


## 安全删除文章
def article_safe_delete(request,id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")
