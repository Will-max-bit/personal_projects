from django.urls import path
from . import views

app_name='roseTattoApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('artists_page/', views.artists_page, name='artists_page')
]