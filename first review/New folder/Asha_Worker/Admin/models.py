from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Org_Profile(models.Model):
    Auth_Id = models.TextField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    DOB=models.DateField()
    Gender=models.CharField(max_length=10)
    State=models.CharField(max_length=50,null=True)
    District=models.CharField(max_length=50,null=True)
    Mobile=models.IntegerField()
    image=models.ImageField(default='default.png',upload_to='Organizer/Profile')

class Org_Reports(models.Model):
    Auth_Id = models.ForeignKey(Org_Profile,on_delete=models.CASCADE)
    Subject = models.CharField(max_length=20)
    Comment = models.TextField()
    Report = models.FileField(upload_to='Organizer/Reports')
    Date = models.DateField()

class State(models.Model):
    State_Name = models.CharField(max_length=30)

class District(models.Model):
    State = models.ForeignKey(State,on_delete=models.CASCADE)
    District_Name = models.CharField(max_length=30)

class Pan_Mun(models.Model):
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    Panchayath_Name = models.CharField(max_length=30)

class Ward(models.Model):
    Panchayath = models.ForeignKey(Pan_Mun,on_delete=models.CASCADE)
    Ward_Name = models.CharField(max_length=30)
