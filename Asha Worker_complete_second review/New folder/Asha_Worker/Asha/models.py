from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BasicDetails(models.Model):
    Auth_Id = models.TextField(primary_key=True,max_length=12)
    User = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Asha_Worker = models.CharField(max_length=50,null=True)
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=5,null=True)
    Address = models.CharField(max_length=100)
    State = models.CharField(max_length=50)
    Distrct = models.CharField(max_length=50)
    Pan_Mun = models.CharField(max_length=50)
    Ward = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Status = models.CharField(max_length=5,default='Tobit')
    Created_Date = models.DateField()

class FamilyMembers(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=5)
    Relationship = models.CharField(max_length=15)
    Marital = models.CharField(max_length=10,null=True)
    Phone = models.CharField(max_length=15)
    Status = models.CharField(max_length=10,null=True)
class Baby(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE,null=True)
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=5)
    DOB = models.DateField()


class User_Pregnancy(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    LMP = models.DateField()
    Weeks = models.CharField(max_length=5)
    Blood = models.CharField(max_length=5)
    Weight = models.CharField(max_length=10)
    Health = models.CharField(max_length=30)
    Hospital = models.CharField(max_length=25)
    Doctor = models.CharField(max_length=30)
    Mobile = models.CharField(max_length=15)
    Register_Date = models.DateField()


class User_Palliative(models.Model):
    Auth_Id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    DOB = models.DateField()
    Mobile = models.CharField(max_length=15)
    Issue = models.CharField(max_length=20)
    Comments = models.CharField(max_length=35)
    Register_Date = models.DateField()

class User_Asha_Notifications(models.Model):
    Owner = models.CharField(max_length=20)
    Title = models.CharField(max_length=20)
    Message = models.TextField()
    Date = models.DateTimeField()