from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hellow Guest !!! Very Good'
    if h<12:
        msg=msg+'Morning!!!'
    elif h<16:
        msg=msg+'Afternoon!!!'
    elif h<21:
        msg=msg+'Evening!!!'
    else:
        msg=msg+'Night!!!'
    my_dict={'m':msg,'date':date}
    
    return render(request,'testapp/results.html',my_dict)
