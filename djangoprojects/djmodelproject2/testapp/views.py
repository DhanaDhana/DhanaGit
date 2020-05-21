from django.shortcuts import render
from testapp.models import djstudent

# Create your views here.
def student_view(request):
    students=djstudent.objects.all()
    return render(request,'testapp/results.html',{'students':students})
