from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
# Create your views here.

def index(request):
    now = random.randint(1,10)
    if now % 2 == 0:
        oddEven = 'EVEN'
    else:
        oddEven = "ODD"
    return render(request, "newyear/index.html", {
        "newyear": oddEven
    })
