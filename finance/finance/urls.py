"""finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users.views import *
from expenses.views import *
from split.views import *
from savings.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #users paths
    path('users/', include('users.urls')),
    path('', index, name='index'),
    path('login/', loginPage, name='login'),
    path('home', index, name='home'),
    path('register/', registerPage, name='register'),
    path('loginUser/', loginUser, name='loginUser'),
    path('logoutUser/', logoutUser, name='logoutUser'),
    path('registerUser/', registerUser, name='registerUser'),
    #expenses paths
    path('expenses/', include('expenses.urls')),
    path('newExpense/', newExpense, name='newExpense'),
    #Split paths
    path('split/', include('split.urls')),

    #Savings paths
    path('savings/', include('savings.urls')),
    path('setNewGoal/', setNewGoal, name="setNewGoal"),
    path('newGoal/', goalSettingPage, name="newGoal"),
]
