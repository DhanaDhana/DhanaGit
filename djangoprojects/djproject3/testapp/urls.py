
from django.urls import path
from testapp import views

urlpatterns = [
    path('sandy/', views.sandhya),
    path('dhana/', views.dhana),
    path('varshita/',views.varshita),
]
