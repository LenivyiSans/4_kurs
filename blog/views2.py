from django.shortcuts import render
from django.http import HttpResponse
import datetime


def nowdate_view(request):

    if request.method == 'GET':

        return HttpResponse(datetime.date.today())