from django.db import models

# Create your models here.
class Donation(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
    Addr1 = models.CharField(max_length=50)
    Addr2  = models.CharField(max_length=50)
    Country  = models.CharField(max_length=30)
    State  = models.CharField(max_length=30)
    Pin = models.CharField(max_length=10)
    Amount = models.CharField(max_length=10,null=True)
    Card = models.CharField(max_length=30)
    Card_Name = models.CharField(max_length=30)