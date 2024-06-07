from django import forms    # Импортируем формы Django
from django.forms import ModelForm
from .models import Article


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')  # Текст комментария


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         STATE_TYPE = (
#             ('draft', 'draft'),
#             ('published', 'published')
#         )
#         model = Category
#         fields = ['name', 'description', 'state']
#         widgets = {
#             "name": forms.CharField(max_length=100),
#             'description': forms.CharField(max_length=200),
#         }
