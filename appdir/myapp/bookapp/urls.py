from django.urls import path
from . import views
urlpatterns = [ 
    path("",views.index, name="index"),
    path("therapistData/",views.therapistData, name="therapistData"),
    path("submit",views.submit, name="submit")
]