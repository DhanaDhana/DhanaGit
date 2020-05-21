from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1> Hello Friend Good Morning!!!<h1>')
def good_evening_view(request):
    return HttpResponse('<h1> Hello Friend Good Evening!!!<h1>')
def good_night_view(request):
    return HttpResponse('<h1> Hello Friend Good Night!!!<h1>')
