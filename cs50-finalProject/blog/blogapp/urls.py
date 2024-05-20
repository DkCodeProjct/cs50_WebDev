from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path("postContent/<int:postId>/", views.postContent, name="postContent"),
    path("userPosts/", views.userPosts, name="userPosts"),
    path("deletePost/<int:postId>/", views.deletePost, name="deletePost"),
    path("confirmDel/<int:postId>/", views.confirmDel, name="confirmDel")
]