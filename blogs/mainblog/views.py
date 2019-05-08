from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from mainblog.models import Article

# Create your views here.
def hello_world(request):
    return HttpResponse('hello world!')

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.acticle_id
    publish_date = article.publish_date
    return_str = 'title: %s, brief_content: %s,'\
            'content: %s, article_id: %s, publish_date: %s' % (
                title,
                brief_content,
                content,
                article_id,
                publish_date
            )
    return HttpResponse(return_str)

def get_index_page(request):
    all_article = Article.objects.all()
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1

    pager = Paginator(all_article, 1)
    page_article_list = pager.page(page)
    next_page = 1
    prev_page = 1
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        prev_page = page - 1
    else:
        prev_page = page
    return render(request, 'mainblog/index.html', {
        'article_list': all_article,
        'page_article_list': page_article_list,
        'page_nums': range(1, pager.num_pages + 1),
        'current_page': page,
        'next_page': next_page,
        'prev_page': prev_page
    })

def get_detail_page(request, acticle_id):
    all_article = Article.objects.all()
    current_article = None
    previous_index = 0
    next_index = 0
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1

        if article.acticle_id == acticle_id:
            current_article = article

    section_list = current_article.content.split('\n')
    return render(request, 'mainblog/detail.html', {
        'current_article': current_article,
        'section_list': section_list,
        'previous_article': all_article[previous_index],
        'next_article': all_article[next_index]
    })