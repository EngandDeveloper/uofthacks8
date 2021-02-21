from django.urls import path

from . import views

urlpatterns = [
    path('newpay', views.split, name="split"),
    path('',views.pendingpay, name="pendingpay"),
]