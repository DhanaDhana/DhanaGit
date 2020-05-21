from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    ceo=models.CharField(max_length=60)
    def __str__(self):
        return self.name
class Employee(models.Model):
    eno=models.IntegerField()
    name=models.CharField(max_length=60)
    salary=models.FloatField()
    company=models.ForeignKey(Company,related_name='employees',on_delete=models.CASCADE)
