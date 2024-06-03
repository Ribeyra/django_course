from django.shortcuts import render, get_object_or_404
from django.views import View

# Create your views here.
from django.http import HttpResponse     # noqa f401

from .models import Article    # Comment


def index(request, tags, article_id):
    # app_name = request.resolver_match.app_name
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
    # return render(
    #     request,
    #     'articles/index.html',
    #     context={
    #         'app_name': app_name
    #     }
    # )


class IndexView(View):
    # def get(self, request, *args, **kwargs):
    #     app_name = request.resolver_match.app_name
    #     return render(
    #         request,
    #         'articles/index.html',
    #         context={
    #             'app_name': app_name
    #         }
    #     )

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={
                'article': article,
            }
        )


# class ArticleCommentsView(View):
#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(
#             Comment,
#             id=kwargs['id'],
#             article__id=kwargs['article_id']
#         )
#         return render(
#             request,
#             'articles/show_comment.html',
#             context={
#                 'comment': comment,
#             }
#         )
