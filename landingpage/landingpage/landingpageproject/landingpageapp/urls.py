from django.urls import path
from . import views

app_name = 'landingpageapp'
urlpatterns = [
    path('', views.index, name='index')
]
