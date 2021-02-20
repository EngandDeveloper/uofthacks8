from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SharedExp(models.Model):
    primary_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(decimal_places=2)
    other_users = models.ManyToManyField(User)
