from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.conf import settings

class UserProfile(models.model):
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
    def __str__(self) -> str:
        return self.user.username + ' - ' + str(self.profile_picture.name)

class Post(models.model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)