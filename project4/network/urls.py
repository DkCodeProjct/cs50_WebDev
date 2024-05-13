
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newPost", views.newPost, name="newPost"),
    path("rmLike/<int:postId>", views.rmLike, name="rmLike"),
    path("adLike/<int:postId>", views.adLike, name="adLike"),
    path("userProfile/<int:userId>", views.userProfile, name="userProfile"),
    path("unFollow", views.unFollow, name="unFollow"),
    path("follow", views.follow, name="follow"),
    path("following", views.following, name="following"),
    path("editPost/<int:postId>", views.editPost, name="editPost"),
]