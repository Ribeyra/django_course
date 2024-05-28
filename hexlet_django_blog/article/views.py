from django.shortcuts import render     # noqa f401

# Create your views here.
from django.http import HttpResponse     # noqa f401


def index(request):
    app_name = request.resolver_match.app_name
    # return HttpResponse('article')
    return render(
        request,
        'articles/index.html',
        context={
            'app_name': app_name
        }
    )
