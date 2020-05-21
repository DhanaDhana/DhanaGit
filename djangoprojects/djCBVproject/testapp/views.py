from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<body align="center"><h1 style="color:red;background:cyan;border:3px solid yellow"> This is From ClassBasedView</h1></body>')
