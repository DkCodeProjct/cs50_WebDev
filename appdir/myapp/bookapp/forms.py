from django import forms
from .models import Therapist, Book_A_Session

class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = '__all__'  # Include all fields from the Therapist model

class Book_A_sessionForm(forms.ModelForm):
    class Meta:
        model = Book_A_Session
        fields = ['patient', 'therapist', 'dateForSession', 'payment_method']