from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Asha_Profile(models.Model):
    Auth_Id = models.TextField(primary_key=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50,null=True)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    Qual = models.CharField(max_length=10)
    Mobile = models.CharField(max_length=15)
    Aadhar = models.CharField(max_length=20)
    Blood = models.CharField(max_length=5)
    Addr1 = models.CharField(max_length=50)
    Addr2  = models.CharField(max_length=50)
    Addr3  = models.CharField(max_length=50)
    Panchayath  = models.CharField(max_length=50,null=True)
    Ward  = models.CharField(max_length=50,null=True)
    Owner  = models.CharField(max_length=50,null=True)
    Pin = models.CharField(max_length=15)
    Aadhar_Id = models.FileField(upload_to='Asha/Id/Documents')
    Addres_Id = models.FileField(upload_to='Asha/Addres/Documents')
    Bank_Account = models.CharField(max_length=50)
    Bank_Name = models.CharField(max_length=20)
    Account_Number = models.CharField(max_length=50)
    IFSC = models.CharField(max_length=50)
    Branch = models.CharField(max_length=50)


class Asha_Insurance(models.Model):
    Auth_Id = models.ForeignKey(Asha_Profile,on_delete=models.CASCADE)
    Plan = models.CharField(max_length=15)
    Amount_Paid = models.CharField(max_length=10)
    Date = models.DateField()

class Asha_Reports(models.Model):
    Auth_Id = models.ForeignKey(Asha_Profile,on_delete=models.CASCADE)
    Subject = models.CharField(max_length=20)
    Comment = models.TextField()
    Feedback = models.TextField(null=True)
    Report = models.FileField(upload_to='Asha/Reports')
    Date = models.DateField()
    Status = models.CharField(max_length=20,null=True)

class Asha_Contact_User(models.Model):
    Auth_Id = models.ForeignKey(Asha_Profile,on_delete=models.CASCADE)
    Subject = models.CharField(max_length=20)
    Message = models.TextField()
    User_Info = models.CharField(max_length=20)
    Date = models.DateTimeField()
    Status = models.CharField(max_length=20,null=True)
    Reply = models.TextField(null=True)

class Org_Asha_Notifications(models.Model):
    Owner = models.CharField(max_length=20)
    Title = models.CharField(max_length=20)
    Comments = models.TextField(null=True)
    Description = models.TextField()
    Date = models.DateTimeField()

class Org_Asha_Forms(models.Model):
    Owner = models.CharField(max_length=20)
    Title = models.CharField(max_length=20)
    Form = models.FileField(upload_to='Organizer/Documents/Forms')
    Comments = models.TextField()
    Date = models.DateTimeField()
