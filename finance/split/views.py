from django.shortcuts import render

# Create your views here.
def split(request):
    return render(request, 'split/index.html')