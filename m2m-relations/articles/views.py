from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    list_articles = Article.objects.all().prefetch_related('tags').order_by('-published_at')
    template = 'articles/news.html'
    context = {'object_list': list_articles,
               }

    return render(request, template, context)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    

   
