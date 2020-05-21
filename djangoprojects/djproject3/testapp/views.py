from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sandhya(request):
    return HttpResponse('<html><body bgcolor="black" text="red"><h1> Hello How Are You Sandhya...</h1></body></html>')

def dhana(request):
    return HttpResponse('<html><body bgcolor="black" text="green"><h1> Hello How Are You Dhana...</h1></body></html>')

def varshita(request):
    return HttpResponse('<html><body bgcolor="black" text="yellow"><h1> Hello How Are You Varshita...</h1></body></html>')
