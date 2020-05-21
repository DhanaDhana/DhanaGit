from django.shortcuts import render

# Create your views here.
def regdisp(request):
    return render(request,'reg.html')
def disp(request):
    name=request.POST['t1']
    age=request.POST['t2']
    email=request.POST['t3']
    addr=request.POST['t4']
    data={'name1':name,'age1':age,'email1':email,'addr1':addr}
    return render(request,'disp.html',data)
