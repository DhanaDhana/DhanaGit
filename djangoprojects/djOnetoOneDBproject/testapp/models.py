from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.sname
class Course(models.Model):
    Student=models.OneToOneField(Student,on_delete=models.SET(9),null=True)
    cname=models.CharField(max_length=20)
    cfee=models.IntegerField()
    def __str__(self):
        return  self.cname
