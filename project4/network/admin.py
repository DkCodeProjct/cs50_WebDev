from django.contrib import admin

from . models import NewPost,NewPostAdmin,User, Follow, Like

# Register your models here.
admin.site.register(NewPost, NewPostAdmin)
admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Like)