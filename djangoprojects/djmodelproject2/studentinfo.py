import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djmodelproject2.settings')
import django
django.setup()

from testapp.models import djstudent
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        frollno=fake.random_int(min=1,max=999)
        fname=fake.name()
        fmarks=fake.random_int(min=1,max=100)
        fphonenumber=phonenumbergen()
        femail=fake.email()
        faddress=fake.address()
        student_record=djstudent.objects.get_or_create(rollno=frollno,name=fname,marks=fmarks,phonenumber=fphonenumber,email=femail,address=faddress)
populate(30)
