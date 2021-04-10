from django.urls import path
from . import views

app_name = 'LFGapp'
urlpatterns=[
    path('index/', views.index, name='index'),
]