from django.http.response import HttpResponse
from django.shortcuts import redirect


def Unauthenticated_user(func):
    def Wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return func(request,*args,**kwargs)
    return Wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(func):
        def Wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return func(request,*args,**kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
        return Wrapper_func
    return decorator

def admin_only(func):
    def Wrapper_func(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=="customer":
            return redirect("user_page")
        if group=="admin":
            return func(request,*args,*kwargs)
    return Wrapper_func

