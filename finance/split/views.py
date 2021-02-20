from django.shortcuts import render

# Create your views here.
urlpatterns = [
    path('', views.expenses, name="expenses"),
    
]