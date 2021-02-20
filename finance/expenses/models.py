from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    description = models.CharField(max_length=300, null=False, blank=True)
    amount = models.DecimalField(null=False, blank=True, decimal_places=2, max_digits=10)
    budgetCategory = models.CharField(max_length=300, null=True, default="None")
    isShared = models.BooleanField(null=False, default=False)
    sharedWith = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField()

    objects = models.Manager()