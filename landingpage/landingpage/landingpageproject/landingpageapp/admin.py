from django.contrib import admin
from .models import CodeWars, Language, Post, Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(CodeWars)
admin.site.register(Language)
