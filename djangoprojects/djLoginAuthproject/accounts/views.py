from django.shortcuts import render,redirect
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def indexView(request):
    return render(request,'index.html')
@login_required
def dashboardView(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hello Guest !!! Very Good'
    if h<12:
        msg=msg+'Morning!!!'
    elif h<16:
        msg=msg+'Afternoon!!!'
    elif h<21:
        msg=msg+'Evening!!!'
    else:
        msg=msg+'Night!!!'
    return render(request,'dashboard.html',{'m':msg,'date':date})
def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
        return render(request,'registration/register.html',{'form':form})
