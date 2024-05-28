from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


TAGS = ['обучение', 'ООП', 'hexlet']


def about(request):
    return render(
        request,
        'about.html',
        context={
            'tags': TAGS
        }
    )
