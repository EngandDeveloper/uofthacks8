from django.urls import path

from . import views

urlpatterns = [
    path('', views.expenses, name="expenses"),
    path('newExpense/', views.newExpense, name="newExpense"),
    path('dashboard/', views.getExpenses, name="getExpenses")
]