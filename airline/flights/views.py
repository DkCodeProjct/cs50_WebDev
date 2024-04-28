from django.shortcuts import render
from . models import Flight, Airport, Passanger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(req):
    return render(req, "flights/index.html", {
        'flights': Flight.objects.all()
    })

def flight(req, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passanger = Passanger.objects.all()
    non_passanger = Passanger.objects.exclude(flights=flight).all()
    return render(req, 'flights/flights.html',{
        'flight':flight,
        'passanger':passanger,
        'non_passanger': non_passanger
    })

def book(req, flight_id):
    if req.method == "POST":
        flight = Flight.objects.get(pk=flight_id)

        passanger_id = int(req.POST['passanger'])

        passanger = Passanger.objects.get(pk=passanger_id)

        passanger.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))