from django.shortcuts import render,redirect
from .models import Customers,Products,Orders,User
from .forms import OrderForm,CustomerForm,ProductForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import Unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

@Unauthenticated_user
def registerpage(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        # if form.is_valid():
        #     form.save()
        if form.is_valid():
            user = form.save()
            username = request.POST.get('username')

            group = Group.objects.get(name='customer')

            user.groups.add(group)
            # username=request.POST.get('username')
            messages.success(request,"Successfully Account is Created for " + username)
            return redirect("login")
    context={'form':form}
    return render(request,'crmaccounts/register.html',context)

@Unauthenticated_user
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.warning(request,'Username and Pasword is Wrong')
    return render(request,'crmaccounts/login.html')

def logoutpage(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    customer=Customers.objects.get(user=request.user)
    orders=request.user.customers.orders_set.all()
    total_order = len(orders)
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    outfordelilvery = orders.filter(status="OutForDelilvery").count()
    context={'customer':customer,'orders':orders,'total_order':total_order,'delivered':delivered,
             'pending':pending,'outfordelilvery':outfordelilvery}
    return render(request,'crmaccounts/user.html',context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    customers=Customers.objects.all()
    orders=Orders.objects.all()

    total_order=len(orders)
    delivered=orders.filter(status="Delivered").count()
    pending=orders.filter(status="Pending").count()
    outfordelilvery=orders.filter(status="OutForDelilvery").count()

    context={'customers':customers, 'orders':orders,
             'total_order':total_order,
             'delivered':delivered,
             'pending':pending,
             'outfordelilvery':outfordelilvery
             }
    return render(request,'crmaccounts/dashboard1.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products=Products.objects.all()
    context={'products':products}
    return render(request,'crmaccounts/products.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request,str_pk):
    customers=Customers.objects.get(id=str_pk)
    orders=customers.orders_set.all()
    total_orders=orders.count()
    context={'customers':customers,'orders':orders,'total_orders':total_orders}
    return render(request,'crmaccounts/customers.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request, 'crmaccounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request,str_pk):
    order=Orders.objects.get(id=str_pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request, 'crmaccounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request,str_pk):
    order=Orders.objects.get(id=str_pk)
    order.delete()
    return redirect("/")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_customer(request,str_pk):
    customer = Customers.objects.get(id=str_pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, 'crmaccounts/update_customer.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_customer(request,str_pk):
    customer = Customers.objects.get(id=str_pk)
    customer.delete()
    return redirect("/")

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_product(request,str_pk):
    product= Products.objects.get(id=str_pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, 'crmaccounts/update_product.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_product(request,str_pk):
    product = Products.objects.get(id=str_pk)
    product.delete()
    return redirect("/")


