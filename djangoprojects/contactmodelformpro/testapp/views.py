from django.shortcuts import render
from django.http import HttpResponse
from testapp.forms import ContactForm
from testapp.models import ContactData
# Create your views here.
def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form=ContactForm()
            return render(request,'contact.html',{'form':form})
        else:
            return HttpResponse('<h1> Invalid Form</h1>')
    else:
        form=ContactForm()
        return render(request,'contact.html',{'form':form})
