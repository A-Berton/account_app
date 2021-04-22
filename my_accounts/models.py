from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance = models.FloatField()
