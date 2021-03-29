from django.urls import path
from . import views

app_name = 'landingpageapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('load_posts', views.load_posts, name='load_posts'),
    path('new_post', views.new_post, name='new_post')
]
