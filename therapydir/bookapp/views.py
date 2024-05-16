from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from . models import Therapist, Patient, Book_A_Session, User
from . forms import TherapistForm, BookSessionForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(req):
    if req.method == "POST":
        form = TherapistForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('therapistList')
    else:
        form = TherapistForm()
    return render(req, 'bookapp/index.html', {
        "form": form
    })

def therapistList(req):
    therapists = Therapist.objects.all()
    return render(req, 'bookapp/list.html', {
        "therapists": therapists   
    })

def data(req, id):
    therapist = Therapist.objects.get(pk=id)
    return render(req, 'bookapp/data.html', {
        "therapist": therapist
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import BookSessionForm

@login_required
def book(request, id):
    therapist = get_object_or_404(Therapist, pk=id)
    patient, created = Patient.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = BookSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.therapist = therapist
            session.patient = patient
            session.save()
            return redirect('therapistList')
    else:
        form = BookSessionForm()
    
    return render(request, 'bookapp/book.html', {
        'form': form,
        'therapist': therapist
    })


#//////////////////////

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
            return render(request, "bookapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "bookapp/login.html")



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
            return render(request, "bookapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "bookapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "bookapp/register.html")
 