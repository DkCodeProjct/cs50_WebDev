from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('therapistList/', views.therapistList, name='therapistList'),
    path('data/<int:id>/', views.data, name='data'),
    path('book/<int:id>/', views.book, name='book'),
]
