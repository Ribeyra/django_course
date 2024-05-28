from django.urls import path

from hexlet_django_blog.article import views

app_name = 'article'  # Задаем пространство имен для маршрутов приложения

urlpatterns = [
    path('', views.index),
]
