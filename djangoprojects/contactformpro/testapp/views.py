from django.shortcuts import render
from django.http import HttpResponse
from testapp.forms import ContactForm
from testapp.models import ContactData
# Create your views here.
def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name1=request.POST.get('name')
            salary1=request.POST['salary']
            email1=form.cleaned_data['email']
            location1=form.cleaned_data.get('location')
            data=ContactData(name=name1,salary=salary1,email=email1,location=location1)
            data.save()
            form=ContactForm()
            return render(request,'contact.html',{'form':form})
        else:
            return HttpResponse('<h1> Invalid Form</h1>')
    else:
        form=ContactForm()
        return render(request,'contact.html',{'form':form})
