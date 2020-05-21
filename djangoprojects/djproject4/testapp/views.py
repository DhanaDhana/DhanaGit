from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    return HttpResponse("<body bgcolor='yellow'><center><font color='red'> <h1>Hello Dhana Good Morning!!!<hr><br>"+str(date)+"<br>DHANA</h1></font>Dhana</center></body>")
