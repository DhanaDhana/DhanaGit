from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.home,name="home"),
    path('customer/<str_pk>',views.customers,name='customer'),
    path('product',views.products,name='product'),
    path('create_order/', views.create_order, name="create_order"),
    path('update_order/<str_pk>',views.update_order,name="update_order"),
    path('delete_order/<str_pk>',views.delete_order,name="delete_order"),
    path('update_customer/<str_pk>', views.update_customer, name="update_customer"),
    path('delete_customer/<str_pk>', views.delete_customer, name="delete_customer"),
    path('update_product/<str_pk>', views.update_product, name="update_product"),
    path('delete_product/<str_pk>', views.delete_product, name="delete_product"),

    path('register/',views.registerpage, name="register"),
    path('login/',views.loginpage,name="login"),
    path('logoutuser/',views.logoutpage,name="logout"),

    path('user/',views.userpage,name="user_page")



]
