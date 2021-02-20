from django.urls import path

from . import views

urlpatterns = [
    path('', views.split, name="split"),
    path('split/',views.split, name="newSplit")
]