from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

from expenses.models import Expense
# Create your views here.
def expenses(request):
    return render(request, 'expenses/index.html')

def newExpense(request):
    context = {}
    form = Expense()

    if request.method == "POST":
        form = Expense(request.POST)
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        budgetCategory = request.POST.get('budgetCategory')
        isShared = request.POST.get('isShared')
        sharedWith = request.POST.get('sharedWith')
        date = request.POST.get('date')
        form = Expense(user=request.user, description=description, amount=amount, budgetCategory=budgetCategory, isShared=isShared, sharedWith=sharedWith, date=date)
        form.save()
        context = {'form': form}
        return render(request, 'expenses/index.html', context)

    context = {'form': form}
    return render(request, 'expenses/index.html', context)

def getExpenses(request):
    context = {}
    user = request.user
    expenses = Expense.objects.all().filter(user__username__contains=user.username)
    context = {'expenses':expenses}
    return render(request, 'expenses/dashboard.html', context)