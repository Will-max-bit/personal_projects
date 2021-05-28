from django.db import models
from django.contrib.auth.models import User
from django.db.models import constraints
from django.db.models.fields import related
from django.conf import settings
from django.utils import timezone

class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
    is_climber = models.BooleanField('climber', default=False)
    is_setter = models.BooleanField('setter', default=False)
    is_gym = models.BooleanField('gym', default=False)
    def __str__(self) -> str:
        return self.user.username + ' - ' + str(self.profile_picture.name)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    post_image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='post_likes')

class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name='following')
    following_user_id = models.ForeignKey("User", related_name='followers')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'following_user_id'], name="unique_followers")
        ]
        ordering = ['-created']
    def __str__(self) -> str:
        f"{self.user_id} follows {self.following_user_id}"

class Rating(models.Model):
    rating = models.CharField(max_length=4)
    type = models.CharField(max_length=10)