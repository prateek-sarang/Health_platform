# core/models.py

# core/models.py

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.SET_NULL)
    response_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='responses')