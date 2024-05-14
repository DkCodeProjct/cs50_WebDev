from django.contrib import admin
from .models import Therapist, Book_A_Session, Patient

 # Register your models here.


admin.site.register(Therapist)
admin.site.register(Book_A_Session)
admin.site.register(Patient)
