from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='blogapp_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='blogapp_users',
        blank=True
    )

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=100)
    post = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)