from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'Hello There General Kenobi'
    }
    return render(request, 'LFGapp/index.html', context)
