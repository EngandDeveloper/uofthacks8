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
    #Budget Categories
    rent = 0
    food = 0
    transportation = 0
    entertainment = 0
    emergencies = 0
    other = 0
    for i in expenses:
        if i.budgetCategory == "Rent":
            rent += i.amount
        elif i.budgetCategory == "Food":
            food += i.amount
        elif i.budgetCategory == "Transportation":
            transportation += i.amount
        elif i.budgetCategory == "Entertainment":
            entertainment += i.amount
        elif i.budgetCategory == "Emergencies":
            emergencies += i.amount
        elif i.budgetCategory == "Other":
            other += i.amount
    budgets = [rent, food, transportation, entertainment, emergencies, other]
    context = {'expenses':expenses, 'budgets':budgets}
    return render(request, 'expenses/dashboard.html', context)