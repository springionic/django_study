from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(request):
    article = Article.objects.get(id=1)
    return render(request, 'blog/index.html', {'article': article})
