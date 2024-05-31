from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article

# Register your models here.

# admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Перечисляем поля, отображаемые в таблице списка статей
    list_display = ('name', 'timestamp')

    search_fields = ['name', 'body']

    # Перечисляем поля для фильтрации
    list_filter = (('timestamp', DateFieldListFilter),)


# admin.site.register(Article, ArticleAdmin)
