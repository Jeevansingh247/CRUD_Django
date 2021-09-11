from django.db import models


# Create your models here.
class Patient1(models.Model):
    PID=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=75)
    Age=models.IntegerField()
    Address=models.TextField(max_length=100)
    City=models.CharField(max_length=45)
    Disease=models.CharField(max_length=40)
