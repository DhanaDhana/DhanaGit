from django.contrib import admin
from django.urls import path,include
from resource_management_app import views
from registration_login_app import views as views2
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('changepassword/', views2.change_password,name='changepassword'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('admin/', admin.site.urls),
    path('personal-details/', views.personal_details, name='personal_details'),
    path('technical-details/', views.technical_details, name='technical_details'),
    path('recent-project-details/', views.recent_project_details, name='recent_project_details'),
    path('advanced-details/', views.advanced_details, name='advanced_details'),
    path('success/', views.success, name='success'),
    
    path('', views2.home,name='home'),
    path('logout/', views2.logout_user,name='logout'),
    path('Register/', views2.Register_user,name='Register'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addnewemployee/', views.addnewemployee, name='addnewemployee'),
    path('updateemployee/<int:empid>/', views.updateemployee, name='updateemployee'),
    path('deleteemp/<int:empid>/', views.deleteemp, name='deleteemp'),
    
    #project
    path('projects/', views.list_projects, name='list_projects'),
    path('projects_add/', views.add_project, name='add_project'),
    path('projects/update/<int:pk>/', views.update_project, name='update_project'),
    path('projects/delete/<int:pk>/', views.delete_project, name='delete_project'),
]
