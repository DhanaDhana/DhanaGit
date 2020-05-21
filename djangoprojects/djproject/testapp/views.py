from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world_view(request):
    return HttpResponse('''<html><body bgcolor="green" text="red" align="center">
                            <h1> Hello This is Response From Django Application</h1>
                            </body></html>''')
