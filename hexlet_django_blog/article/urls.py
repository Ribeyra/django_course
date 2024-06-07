from django.urls import path

from hexlet_django_blog.article import views

app_name = 'article'  # Задаем пространство имен для маршрутов приложения

urlpatterns = [
    path('', views.IndexView.as_view(), name='article_index'),
    path('<tags>/<int:article_id>', views.index, name='article'),
    path('<int:id>/', views.ArticleView.as_view(), name='view_article'),
    path(
        'create/',
        views.ArticleFormCreateView.as_view(),
        name='articles_create'
    ),
    # path(
    #     '<int:article_id>/comments/<int:id>/',
    #     views.ArticleCommentsView.as_view(),
    #     name='view_comment'
    # ),
]
