from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView
# Create your views here.
class CompanyListView(ListView):
    model=Company
class CompanyDetailView(DetailView):
    model=Company
    
