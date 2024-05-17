from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
 
class Category(models.Model):
    categoryName= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.categoryName
    
   
class Bid(models.Model):
    bid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")

    def __str__(self):
       return f"Bid of {self.bid} from {self.user}"



class CreateListing(models.Model):
    title = models.CharField(max_length=32)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing", null=True, blank=True)
    is_closed = models.BooleanField(default=False, blank=True, null=True)
    desc = models.CharField(max_length=400)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="listing", default=None)
    imgUrl = models.CharField(max_length=800)   
    watchlist = models.ManyToManyField(User, blank=True, related_name="listingWatchlist")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='category')
    isActive = models.BooleanField(default=True)
    
    # // date shows when listing creates
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.bid}"

class Comment(models.Model):
    text = models.CharField(max_length=800) 
    user = models.ForeignKey(User,blank=True,null=True ,on_delete=models.CASCADE, related_name="comment")
    item = models.ForeignKey(CreateListing, blank=True, null=True,on_delete=models.CASCADE, related_name="comment")