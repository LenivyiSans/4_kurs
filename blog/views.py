from django.shortcuts import render
from django.http import HttpResponse
import datetime


def helloView(request):
    return HttpResponse("<h1>hi this is my first django project</h1>")


def nowdate_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.date.today())


def goodbyView(request):
    return HttpResponse("<h1>Goodby user</h1>")


