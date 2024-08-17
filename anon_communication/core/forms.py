# core/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ClientRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class DoctorRegisterForm(UserCreationForm):
    specialization = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'specialization', 'license_number']
