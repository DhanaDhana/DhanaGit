from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Create your views here.
#Login Function
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have login successfully!')
            return redirect('home')
        else:
            messages.success(request, "You couldn't find an account with that username. Try another, or get a new account.")
            return redirect('home')
    else:
        return render(request,'home.html')
    return render(request,'home.html')
    
#Logout Function
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout successfully!')
    return redirect('home')
    
#Register Function
def Register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        password1=request.POST['password1']
        password2=request.POST['password2']
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully Register!')
            return redirect('home')
        elif password1!=password2:
            messages.success(request, 'Your password and confirm password are not same!')
            return redirect('Register')
            
        else:
            messages.success(request, 'You have not enter correct data for Registeration!')
            return redirect('Register')
    else:
        form=SignUpForm()
        return render(request,'Register.html',{'form':form})
    return render(request,'Register.html')


# Change Password
def change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            #update_session_auth_hash(request, fm.user)
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('home')

    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'fm': fm})
            