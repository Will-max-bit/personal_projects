from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category

def index(request):
    return HttpResponse('hello world')
