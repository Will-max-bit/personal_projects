from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Category

def index(request):
    return render(request, 'landingpageapp/index.html')

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