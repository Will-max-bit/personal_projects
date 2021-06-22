from django.urls import path
from . import views

app_name = 'landingpageapp'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('index/', views.index, name='index'),
    path('load_posts', views.load_posts, name='load_posts'),
    path('new_post', views.new_post, name='new_post'),
    path('get_categories', views.get_categories, name='get_categories'),
    path('filtered_posts', views.filtered_posts, name='filtered_posts'),
    path('coding_challenges/', views.coding_challenges, name='coding_challenges'),
    path('code_wars', views.code_wars, name='code_wars'),
    path('projects/', views.projects, name='projects'),
    path('project_pictures', views.project_pictures, name='project_pictures'),
    path('rose_tattoo/', views.rose_tat, name='rose_tat'),
    path('climb_up/', views.climb_up, name='climb_up'),
    path('moogle/', views.moogle, name='moogle')
]
