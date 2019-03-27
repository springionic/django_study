from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    else:
        article = Article.objects.get(id=article_id)
        return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        Article.objects.create(title=title, content=content)
        articles = Article.objects.all()
        return render(request, 'blog/index.html', {'articles':articles})
    else:
        article = Article.objects.get(id=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})

