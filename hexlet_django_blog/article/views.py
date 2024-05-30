from django.shortcuts import render     # noqa f401
from django.views import View

# Create your views here.
from django.http import HttpResponse     # noqa f401


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
    def get(self, request, *args, **kwargs):
        app_name = request.resolver_match.app_name
        return render(
            request,
            'articles/index.html',
            context={
                'app_name': app_name
            }
        )
