from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


def index(request):
    return redirect(
        reverse('article:article', kwargs={'tags': 'python', 'article_id': 42})
    )
    # return render(request, 'index.html', context={
    #     'who': 'World',
    # })


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


TAGS = ['обучение', 'ООП', 'hexlet']


def about(request):
    return render(
        request,
        'about.html',
        context={
            'tags': TAGS
        }
    )
