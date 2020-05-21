from django.shortcuts import render

# Create your views here.
def logindisp(request):
    return render(request,'login.html')
def disp(request):
    name=request.POST['uname']
    pwd=request.POST['upwd']
    if  name == 'dhana' and pwd == '1525':
        return render(request,'success.html')
    else:
        return render(request,'failure.html')
