from django.shortcuts import render     # noqa f401

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('article')
