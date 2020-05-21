from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView
# Create your views here.
class BoookListView(ListView):
    model=Book
