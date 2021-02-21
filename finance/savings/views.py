from django.shortcuts import render
import math

from savings.models import Goal
# Create your views here.
def fvapmt(fv,r,t):
    return ((fv*r)/((1+r)**t-1))

def savings(request):
    context = {}
    user = request.user
    goals = Goal.objects.all().filter(user__username__contains=user.username)
    payments = []
    data = []
    for g in goals:
        fv = g.amount
        r = (g.rate/100)
        t = g.time
        answer = fvapmt(fv,r,t)
        formatted = str(round(answer, 2))
        payments.append(formatted)
        data.append([g,formatted])

    context = {'goals':goals, 'payments':payments, 'data':data}
    return render(request, 'savings/index.html', context)

def goalSettingPage(request):
    return render(request, 'savings/setGoal.html')

def setNewGoal(request):
    context = {}
    form = Goal()
    if request.method == "POST":
        form = Goal(request.POST)
        goalname = request.POST.get('goalname')
        amount = request.POST.get('amount')
        time = request.POST.get('time')
        rate = request.POST.get('rate')
        form = Goal(user=request.user, goalname=goalname, amount=amount, time=time, rate=rate)
        form.save()
        context = {'form': form}
        return savings(request)
    return savings(request)