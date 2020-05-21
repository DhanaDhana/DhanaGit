from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request,username="DefaultName",article='DefaultArticle'):
    return HttpResponse('<h1>This is profile page!The username is : {} , The article name is :{}  </h1>'.format(username,article))
    #return HttpResponse('<h1>This is profile page!The username is : %s , The article name is :%s  </h1>'%(username,article))
    
