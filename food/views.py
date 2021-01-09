from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    item_list = models.Item.objects.all()
    return HttpResponse(item_list)

def items(request):
    return HttpResponse('<h1>items<h1>')
