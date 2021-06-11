from django.db import models
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title


class Language(models.Model):
    language_name = models.CharField(max_length=50)
    language_logo = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    def __str__(self):
        return self.language_name

class CodeWars(models.Model):
    title = models.CharField(max_length=30)
    code_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    rank = models.CharField(max_length=5)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='coding_language')

    def __str__(self):
        return self.title + self.rank

class projects_video(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
    
    def __str__(self):
        return self.title

class projects_pictures(models.Model):
    title = models.CharField(max_length=30)
    project_image = models.ImageField(upload_to='post_images/', null=True, blank=True)