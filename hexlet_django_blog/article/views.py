from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

# Create your views here.
from django.http import HttpResponse     # noqa f401

from .models import Article, Comment
from .forms import CommentArticleForm, ArticleForm


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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        # Если данные корректные, то сохраняем данные формы
        if form.is_valid():
            form.save()
            # Редирект на указанный маршрут
            return redirect('article:article_index')
        # Если данные некорректные, то возвращаем человека обратно на
        # страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        # Создаем экземпляр нашей формы
        form = CommentArticleForm()
        # Передаем нашу форму в контексте
        return render(request, 'comment.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # Получаем данные формы из запроса
        form = CommentArticleForm(request.POST)
        if form.is_valid():     # Проверяем данные формы на корректность
            # Получаем очищенные данные из поля content
            comment = Comment(
                text=form.cleaned_data['content'],
                # Заполняем оставшиеся поля
                )
            comment.save()


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
