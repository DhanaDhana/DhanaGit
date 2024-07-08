
from django.contrib import admin
from django.urls import path
from registration_login_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('changepassword/', views.change_password,name='changepassword'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    
    path('', views.home,name='home'),
    path('logout/', views.logout_user,name='logout'),
    path('Register/', views.Register_user,name='Register'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    
]

