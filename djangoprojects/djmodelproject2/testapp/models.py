from django.db import models

# Create your models here.
class djstudent(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=20)
    marks=models.IntegerField()
    phonenumber=models.BigIntegerField()
    email=models.EmailField(max_length=60)
    address=models.TextField()
