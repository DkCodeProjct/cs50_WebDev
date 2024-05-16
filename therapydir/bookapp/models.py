from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    pass

class Patient(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

class Book_A_Session(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient_session")
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, related_name="therapist")
    dateForSession = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    patient_name = models.CharField(max_length=150)
    therapist_name = models.CharField(max_length=150)

    