from django.shortcuts import render
from django.contrib.auth.models import User
from split.models import SharedExp, PendingPay

# Create your views here.


def split(request):
    users = User.objects.all()
    user_dictionary = {
        'users': users
    }
    if request.method == "POST":
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        print(title)
        form = SharedExp(primary_user=request.user, name=title, amount=amount)
        form.save()
        num_users = 0
        for i in users:
            if "FriendId" == request.POST.get(i.username):
                num_users += 1
        for i in users:
            print(request.POST.get(i.username))
            if "FriendId" == request.POST.get(i.username):
                print("accepted username")
                form.other_users.add(i)
                pending = PendingPay(user=i,recipient=request.user,amount=int(amount)/(num_users+1))
                pending.save() 
        form.save()
        return render(request, 'split/index.html',user_dictionary)
    return render(request, 'split/index.html', user_dictionary)