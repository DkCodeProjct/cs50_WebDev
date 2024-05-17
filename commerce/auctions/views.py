from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Comment, CreateListing, Bid, Category

# project done[maybe(researchMore)] push-git

def listing(req, id):
    listingData =CreateListing.objects.get(pk=id)
    isListingInWatchlist = req.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(item=listingData)
    isOwner = req.user.username == listingData.owner.username
    return render(req, "auctions/listings.html", {
        "listing": listingData,
        "isListingInWatchlist": isListingInWatchlist,
        "allComments": allComments,
        "isOwner": isOwner
    })




def closeAuction(req, id):
    listingData = CreateListing.objects.get(pk=id)
    listingData.isActive = False
    listingData.save()
    isOwner = req.user.username == listingData.owner.username
    isListingInWatchlist = req.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(item=listingData)
    return render(req, "auctions/listings.html", {
        "listing": listingData,
        "isListingInWatchlist": isListingInWatchlist,
        "allComments": allComments,
        "isOwner": isOwner,
        "update": True,
        "message": "auction closed"
    })







def addBid(req, id):
    newBid = req.POST['newBid']
    listingData = CreateListing.objects.get(pk=id)
    isListingInWatchlist = req.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(item=listingData)
    isOwner = req.user.username == listingData.owner.username
    if int(newBid) > listingData.bid.bid:
        updateBid = Bid(user=req.user, bid=int(newBid))
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(req, "auctions/listings.html", {
            "listing": listingData,
            "message": "bid update success",
            "update": True,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments,
            "isOwner": isOwner,
        })
    else:
        return render(req, "auctions/listings.html", {
                    "listing": listingData,
                    "message": "bid update failed",
                    "update": False,
                    "isListingInWatchlist": isListingInWatchlist,
                    "allComments": allComments,
                    "isOwner": isOwner,
                })





def addComment(req, id):
    currentUser = req.user
    listingData = CreateListing.objects.get(pk=id)
    msg = req.POST['newComment']

    newComment = Comment(
        user = currentUser,
        item = listingData,
        text = msg
    )

    newComment.save()

    return HttpResponseRedirect(reverse("listing", args=(id, )))

def displayWatchlist(req):
    currentUser = req.user
    listings = currentUser.listingWatchlist.all()
    return render(req, "auctions/watchlist.html", {
        "listings": listings
    })






def removeWatchlist(req, id):
    listingData = CreateListing.objects.get(pk=id)
    currentUser = req.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))



def addWatchlist(req, id):
    listingData = CreateListing.objects.get(pk=id)
    currentUser = req.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))



def index(req):
    activeListings = CreateListing.objects.filter(isActive=True)
    allCategories = Category.objects.all()
    return render(req, "auctions/index.html", {
        "listings": activeListings,
        "categories": allCategories,
    })

def displayCategory(req):
    if req.method == "POST":
        catFromForm = req.POST.get('category')  # Use get() to avoid KeyError if 'category' is not in POST data
        activeListings = CreateListing.objects.filter(isActive=True)
        if catFromForm:
            category = Category.objects.get(categoryName=catFromForm)
            activeListings = activeListings.filter(category=category)
        categories = Category.objects.all()
        return render(req, "auctions/index.html", {
            "listings": activeListings,
            "categories": categories,
        })



def createListing(req):
    if req.method == "GET":
        categories = Category.objects.all()
        return render(req, "auctions/create.html", {
            "categories": categories
        })
    else:
        title = req.POST['title']
        desc= req.POST.get('desc')
        imgUrl = req.POST['imgUrl']
        bid = req.POST['bid']
        category = req.POST['category']
        
        currentUser = req.user
        
        categoryData = Category.objects.get(categoryName=category)
        
        

        bid = Bid(bid=int(bid), user=currentUser)
        bid.save()


        addlist = CreateListing(
            title=title,
            desc=desc,
            imgUrl=imgUrl,
            bid=bid,
            category=categoryData,
            owner = currentUser
        )

        addlist.save()

        return HttpResponseRedirect(reverse(index))

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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
