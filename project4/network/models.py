from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import dateformat
from django.contrib import admin    


class User(AbstractUser):
    pass

class NewPostAdmin(admin.ModelAdmin):
    exclude = ('date',)

class NewPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    post = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        formatDate = dateformat.format(self.date, 'd F Y, H:i')

        return f" User:{self.user}, Post:{self.post} in {formatDate}"
   

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_User") #im following 
    userFollower = models.ForeignKey(User, on_delete=models.CASCADE , related_name="followed_User") # this guy

    def __str__(self):
        return f"{self.user}: following {self.userFollower}"

    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likeUser")
    post = models.ForeignKey(NewPost,on_delete=models.CASCADE, related_name="likePost")

    def __str__(self):
        return f"{self.user} like {self.post}"
