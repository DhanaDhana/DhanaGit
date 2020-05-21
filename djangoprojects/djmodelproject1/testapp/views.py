from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def emp_info_view(request):
    #add record 1st way
    #e=Employee(eno=107,ename="Ayesha",esal=7000,eaddr="Hindupure")
    #e.save()
    #add record 2st way
    #Employee.objects.create(eno=108,ename="Aeisha",esal=8000,eaddr="Hindupure")
    employees=Employee.objects.all().order_by('-esal')[0:3]
    #add multiple records
    #Employee.objects.bulk_create([Employee(eno=109,ename="Chandana",esal=9000,eaddr="nelluru"),Employee(eno=110,ename="Sravanti",esal=10000,eaddr="Rayachoty")])

    return render(request,'testapp/results.html',{'employees':employees})
