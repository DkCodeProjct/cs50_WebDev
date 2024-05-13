from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,NewPost, Like, Follow
from django.core.paginator import Paginator # give nxt//prvius btn if pages > X_Num 
import json
from django.http import JsonResponse



def rmLike(req, postId):
    post = NewPost.objects.get(pk=postId)
    user = User.objects.get(pk=req.user.id) 
    like = Like.objects.get(user=user, post=post)
    like.delete()

    return JsonResponse({"message": "like removed"})



def adLike(req, postId):
    post = NewPost.objects.get(pk=postId)
    user = User.objects.get(pk=req.user.id)
    addLike = Like(user=user,post=post)
    addLike.save()


def index(request):
    allPosts = NewPost.objects.all().order_by("id").reverse()
    
    paginator = Paginator(allPosts, 10) 
    pgNum = request.GET.get('page')
    pgObject = paginator.get_page(pgNum) 

    likes = Like.objects.all()

    likeUser = []

    try:
        for like in likes:
            if like.user.id == request.user.id:
                likeUser.append(like.post.id)
    except:
        likeUser = []

    return render(request, "network/index.html",{
        "allPosts":allPosts,
        "pgObject":pgObject,
        "likeUser":likeUser
    })

def newPost(req):
    if req.method == "POST":
        post = req.POST['post']
        user = User.objects.get(pk=req.user.id)
        post = NewPost(post=post, user=user)
        post.save()
        return HttpResponseRedirect(reverse(index))


def editPost(req, postId):
    if req.method == "POST":
        # Assuming you're sending JSON data from the client side
        jsData = json.loads(req.body)
        editPost = NewPost.objects.get(pk=postId)
        editPost.post = jsData["postContent"]
        editPost.save()

        return JsonResponse({"message": "change saved", "data": jsData["postContent"]})



def userProfile(req, userId):

    user = User.objects.get(pk=userId)
    allPosts = NewPost.objects.filter(user=user).order_by("id").reverse()
    paginator = Paginator(allPosts, 10)
    pgNum = req.GET.get('page')
    pgObject = paginator.get_page(pgNum)
    
    following = Follow.objects.filter(user=user)
    followers = Follow.objects.filter(userFollower=user)
    # pagiantor for user profile  //
    paginator = Paginator(allPosts, 10) 
    pgNum = req.GET.get('page')
    pgObject = paginator.get_page(pgNum)

    try:
        checkFolloing = followers.filter(user=User.objects.get(pk=req.user.id))
        if len(checkFolloing) != 0:
            isFollowing = True

        else:
            isFollowing = False
    except:
        isFollowing = False 

    return render(req, "network/userProfile.html",{
        "allPosts":allPosts,
        "pgObject":pgObject,
        "username":user.username, 
        "profileOwner":user,
        "following":following,
        "followers":followers,
        "isFollowing": isFollowing,
        "profile":user
    })

# follownig woks
def following(request):
    curntUser = User.objects.get(pk=request.user.id)
    followingPpl = Follow.objects.filter(user=curntUser)
    allPosts = NewPost.objects.all().order_by('id').reverse()
    
    followingPosts = []

    for post in allPosts:
        for person in followingPpl:
            if person.userFollower == post.user: #userFollower is from model
                followingPosts.append(post)

    # Pagination for following
    paginator = Paginator(followingPosts, 10)
    pgNum = request.GET.get('page')
    pgObject = paginator.get_page(pgNum) 

    return render(request, "network/following.html", {
        "pgObject":pgObject #page objects or posts in page
    })
    
# unfollow owrks as well
def unFollow(req):
    userFollow = req.POST['userFollow']
    currntUser = User.objects.get(pk=req.user.id)
    userFollowingData = User.objects.get(username=userFollow)
    follow = Follow.objects.get(user=currntUser, userFollower=userFollowingData)  # Corrected field name
    follow.delete()

    userId = userFollowingData.id
    return HttpResponseRedirect(reverse(userProfile, kwargs={'userId':userId}))


def follow(req):
    userFollow = req.POST['userFollow']
    currntUser = User.objects.get(pk=req.user.id)
    userFollowingData = User.objects.get(username=userFollow)
    follow = Follow(user=currntUser, userFollower=userFollowingData)  # Corrected field name
    follow.save()

    userId = userFollowingData.id
    return HttpResponseRedirect(reverse(userProfile, kwargs={'userId':userId}))



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

   

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
