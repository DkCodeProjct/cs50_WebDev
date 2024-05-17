from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CreateListing, Bid, Category
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(CreateListing)
admin.site.register(Bid)
admin.site.register(Category)