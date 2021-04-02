from django.urls import path
from . import views

app_name = 'landingpageapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('load_posts', views.load_posts, name='load_posts'),
    path('new_post', views.new_post, name='new_post'),
    path('get_categories', views.get_categories, name='get_categories'),
    path('filtered_posts', views.filtered_posts, name='filtered_posts')
]
