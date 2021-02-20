from django.urls import path

from . import views

urlpatterns = [
    path('', views.expenses, name="expenses"),
    path('expenses/', views.expenses, name="expenses"),
    path('exp/', views.expenses, name="expenses"),
]