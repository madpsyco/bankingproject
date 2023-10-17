from django.db import models

# Create your models here.
class Formdata(models.Model):
    name=models.CharField(max_length=250,null=True)
    age=models.DateField(null=True)
    gender = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    email=models.EmailField(null=True)
    address=models.CharField(max_length=300)
    district=models.CharField(max_length=300,null=True)
    branch=models.CharField(max_length=100,null=True)
    account=models.CharField(max_length=100)
    atmcard=models.BooleanField(default=False,null=True)
    checkbook=models.BooleanField(default=False,null=True)

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

