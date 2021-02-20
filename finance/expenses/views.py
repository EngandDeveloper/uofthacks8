from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def expenses(request):
    return render(request, 'expenses/index.html')