from django.urls import path

from . import views

urlpatterns = [
    path('', views.savings, name="savings"),
    path('setNewGoal/', views.setNewGoal, name="setNewGoal"),
    path('newGoal/', views.goalSettingPage, name="newGoal"),
]