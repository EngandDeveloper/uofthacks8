from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    goalname = models.CharField(max_length=300, null=False, blank=True)
    amount = models.DecimalField(null=False, blank=True, decimal_places=2, max_digits=10)
    time = models.IntegerField(null=False, blank=True)
    rate = models.DecimalField(null=False, blank=True, decimal_places=2, max_digits=10)

    objects = models.Manager()