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
    