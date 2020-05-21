from django.shortcuts import render
from django.core.mail import send_mail
import smtplib
# Create your views here.
def send(request):
    send_mail('djangoproject','This is django project body i like python and django and datasciencie','dhanakondareddy825@gmail.com',['dhanakondareddy825@gmail.com'],fail_silently=False)
