from django.shortcuts import render
from django.http import HttpResponse


def helloView(request):
    return HttpResponse("<h1>hi this is my first django project</h1>")