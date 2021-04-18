from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'roseTattoApp/index.html')

def artists_page(request):
    return render(request, 'roseTattoApp/artists_page.html')

def artist1(request):
    return render(request, 'roseTattoApp/artist1.html')