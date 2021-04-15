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



class State(models.Model):
    State_Name = models.CharField(max_length=30)

class District(models.Model):
    State = models.ForeignKey(State,on_delete=models.CASCADE)
    District_Name = models.CharField(max_length=30)
