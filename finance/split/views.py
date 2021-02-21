from django.shortcuts import render
from django.contrib.auth.models import User

from split.models import SharedExp
# Create your views here.
def split(request):
    users = User.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        print(title)
        form = SharedExp(primary_user=request.user, name=title, amount=amount)
        form.save()
        for i in users:
            if i.username == request.POST.get(i.username):
                form.other_users.add(i)
        form.save()
        return render(request, 'split/index.html')
    print(users[2].username)
    user_dictionary = {
        'users': users
    }
    return render(request, 'split/index.html', user_dictionary)