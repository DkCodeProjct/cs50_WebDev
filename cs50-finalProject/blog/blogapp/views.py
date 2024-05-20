from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import BlogPostForm
from .models import BlogPost, User
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404

# Create your views here.



def index(request):
    
    posts = BlogPost.objects.all().order_by('-date')
    
    return render(request, 'blogapp/index.html', {
        
        'posts': posts
    
    })


def userPosts(req):
    posts = BlogPost.objects.filter(user=req.user).order_by('-date')
    
    return render(req, 'blogapp/userPost.html',{
        "posts":posts
    })


"""came_back Tracks whethre the user coming frim index[home] or userPosts and render the appropiate back """
def postContent(req, postId):
    post =  get_object_or_404(BlogPost, id=postId)
    came_from = req.GET.get('came_from', 'index') 
    return render(req, 'blogapp/content.html', {
        'post': post,
        'came_from': came_from
    })



@login_required
def create_blog_post(request):
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            blog_post.save()
            return redirect('index')
    
    else:
        form = BlogPostForm()
    
    return render(request, 'blogapp/post.html', {'form': form})

@login_required
def confirmDel(req, postId):
    post = get_object_or_404(BlogPost, id=postId, user=req.user)
    return render(req, 'blogapp/delete.html',{
        "post":post
    })


@login_required
def deletePost(req, postId):
    post = get_object_or_404(BlogPost, id=postId, user=req.user)
    if req.method == 'POST':
        post.delete()
        return redirect('userPosts')
    return redirect(' confirmDel', postId=postId)


#login lgout register views 
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "blogapp/login.html")

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "blogapp/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "blogapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect('index')
    else:
        return render(request, "blogapp/register.html")
