from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello World!')


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = f'title: {title}, brief_content: {brief_content}, \
    content: {content}, publish_date: {publish_date}, article_id: {article_id}'
    return HttpResponse(return_str)


def get_index_page(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 3)
    page_article_list = paginator.page(page)
    page_num = paginator.num_pages
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page-1
    else:
        previous_page = page
    right_list = Article.objects.order_by('-publish_date')[:5]
    context = {
        'article_list': page_article_list,
        'page_num': range(1, page_num+1),
        'curr_page': page,
        'next_page': next_page,
        'previous_page': previous_page,
        'right_list': right_list
    }
    return render(request, 'blog/index.html', context=context)


def get_detail_page(request, article_id):
    curr_article = Article.objects.get(article_id=article_id)
    try:
        previous_article = Article.objects.get(article_id=(int(article_id)-1))
    except:
        previous_article = curr_article
    try:
        next_article = Article.objects.get(article_id=(int(article_id)+1))
    except:
        next_article = curr_article

    section_list = curr_article.content.split('\n')
    context = {
        'curr_article': curr_article,
        'section_list': section_list,
        'previous_article': previous_article,
        'next_article': next_article
    }
    return render(request, 'blog/detail.html', context=context)