# from landingpage.landingpageproject import landingpageapp
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import CodeWars, Post, Category, Projects_pictures
from datetime import datetime
from django.utils.timezone import get_current_timezone
import json
import requests
from django.views.generic.base import TemplateView



def home_page(request):
    return render(request, 'landingpageapp/home_page.html')

def index(request):
    return render(request, 'landingpageapp/index.html')

def coding_challenges(request):
    return render(request, 'landingpageapp/coding_challenges.html')

def projects(request):
    return render(request, 'landingpageapp/projects.html')

def rose_tat(request):
    return render(request, 'landingpageapp/rose_tattoo.html')

def poke(request):
    return render(request, 'landingpageapp/poke_app.html')

def climb_up(request):
    return render(request, 'landingpageapp/climb_up.html')

def moogle(request):
    return render(request, 'landingpageapp/moogle.html')

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
# get title out of database, use title for new function that will return urls
def code_api(request):
    codewars_titles = CodeWars.objects.get('title')
    code_title_data = []
    for title in codewars_titles:
        code_title_data.append({
            'title':title.title,
        })
    return JsonResponse({'codewars_titles': code_title_data })
    
def project_pictures(request):
    project_pictures_posts = Projects_pictures.objects.all()
    project_pictures_data = []
    for picture in project_pictures_posts:
        project_pictures_data.append({
            'title': picture.title,
            'project_image': picture.project_image.url,
        })
    return JsonResponse({'project_pictures': project_pictures_data})

# use codewars api to get user challenges, concatenate the number to a string 'https://www.codewars.com/kata/+num'
# use that as a link for the user to see the code
# see if we can get code image in a modal or maybe use slidr so that the images are thumbnails that enlarge in some way
# 