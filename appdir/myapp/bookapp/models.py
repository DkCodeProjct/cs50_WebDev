from django.db import models


# Create your models here.
class  Patient(models.Model):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField()


class Therapist(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    location = models.CharField(max_length=255)
    email = models.EmailField()
    experience = models.IntegerField()
    specialization = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    licenseNum = models.CharField(max_length=50)
    tradition = models.CharField(max_length=100)
    priceForSession = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Book_A_Session(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, related_name="therapist")
    dateForSession = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], default='pending')
    payment_method = models.CharField(max_length=50, blank=True, null=True)


   