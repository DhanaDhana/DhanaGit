from django.shortcuts import render
from testapp import forms
# Create your views here.
def Studentinputview(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            print(' Form validation success and printing data')
            print("Name : ",form.cleaned_data['name'])
            print("Marks : ",form.cleaned_data['marks'])
    return render(request,'input.html',{'form':form})
