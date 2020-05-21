from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_view(request):
    name='Dhana'
    resp='<h1>Hello</h1>'+name
    return HttpResponse(resp)

def hello_view(request):
    name='Vaishu'
    resp='<h1>Hello</h1>'+name
    return HttpResponse(resp)

def hello_view(request):
    name='Ayesha'
    resp='<h1>Hello</h1>'+name
    return HttpResponse(resp)
