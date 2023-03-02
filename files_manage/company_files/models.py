from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length= 200)
    adress = models.CharField(max_length= 200)

    def __str__(self) :
        return self.name


class File(models.Model):
    file = models.FileField(upload_to='files/%Y/%m/%d')
    upload_date = models.DateField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

TYPE_CHOICES = (
    ("OFFICE", "office"),
    ("ADMIN", "admin"),
)

class User(AbstractUser) :
    type = models.CharField(choices = TYPE_CHOICES, default = 'OFFICE', max_length = 100) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name= "users", null=True)

    def __str__(self) :
        return self.username

