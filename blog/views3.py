from django.shortcuts import render
from django.http import HttpResponse


def goodbyView(request):
    return HttpResponse("<h1>Goodby user</h1>")