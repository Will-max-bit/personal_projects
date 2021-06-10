# from landingpage.landingpageproject import landingpageapp
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CodeWars, Post, Category
from datetime import datetime
from django.utils.timezone import get_current_timezone
import json
import requests

def home_page(request):
    return render(request, 'landingpageapp/home_page.html')

def index(request):
    return render(request, 'landingpageapp/index.html')

def coding_challenges(request):
    return render(request, 'landingpageapp/coding_challenges.html')

def projects(request):
    return render(request, 'landingpageapp/projects.html')

def load_posts(request):
    posts = Post.objects.all().order_by('-created_date')
    post_data = []
    for post in posts:
        post_data.append({
            'title': post.title,
            'text': post.text,
            'id': post.id,
            'category_id': post.category.id,
            'category': post.category.name,
            'post_image': post.post_image.url,
            'created_date': post.created_date.strftime('%b %d %Y'),
        })
    return JsonResponse({'posts': post_data,})

def new_post(request):
    category_id = request.POST['category_id']
    created_date = request.POST['created_date']
    tz = get_current_timezone()
    post = Post(
        title = request.POST['title'],
        text = request.POST['text'],
        post_image = request.FILES['post_image'],
        category = Category.objects.get(id=category_id),
    )
    post.save()
    return HttpResponse('saved')

def get_categories(request):
    categories = Category.objects.all()
    category_data = []
    for category in categories:
        category_data.append({
            'name': category.name,
            'id': category.id,
        })
    
    return JsonResponse({'categories': category_data})

def filtered_posts(request):
    code_wars_posts = Post.objects.filter(category='codewars').order_by('created_date')
    code_wars_data = []
    for post in code_wars_posts:
        code_wars_data.append({
            'title': post.title,
            'text': post.text,
            'id': post.id,
            'category_id': post.category.id,
            'category': post.category.name,
            'post_image': post.post_image.url,
            'created_date': post.created_date.strftime('%b %d %Y'),
        })
    return JsonResponse({'code_wars_posts': code_wars_data})

def code_wars(request):
    code_warsposts = CodeWars.objects.all().order_by('completed_date')
    code_wars_data = []
    for code in code_warsposts:
        code_wars_data.append({
        'title': code.title,
        'code_image':code.code_image.url,
        'completed_date':code.completed_date.strftime('%b %d %Y'),
        'rank': code.rank,
        'language_id': code.language.id,
        'language_name': code.language.language_name,
        'language_logo': code.language.language_logo.url
        })
    return JsonResponse({'codewars_posts': code_wars_data})
