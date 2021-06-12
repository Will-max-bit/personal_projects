from django.contrib import admin
from .models import CodeWars, Language, Post, Category, Projects_pictures, Projects_video

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(CodeWars)
admin.site.register(Language)
admin.site.register(Projects_pictures)
admin.site.register(Projects_video)