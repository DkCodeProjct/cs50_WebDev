from django.shortcuts import render, redirect
from . models import Therapist, Patient, Book_A_Session
from . forms import TherapistForm, Book_A_sessionForm
# Create your views here.
"""
def index(req):
    form = TherapistForm()  # Define form outside of the if-else block
    if req.method == 'POST':
        form = TherapistForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(req, 'bookapp/index.html', {'form': form})
"""

def index(req):
    form = TherapistForm()
    if req.method == 'POST':
        form = TherapistForm(req.POST)
        if form.is_valid():
            form.save()
            # Redirect to the submit success page
            return redirect('submit')
    return render(req, 'bookapp/index.html', {'form': form})

def submit(req):
    return render(req, 'bookapp/submit.html')


def therapistData(req):
    therapists = Therapist.objects.all()
    
    form = Book_A_sessionForm()
    if req.method == 'POST':
        form = Book_A_sessionForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('submit')
    
    return render(req, 'bookapp/data.html', {'therapists': therapists})

         