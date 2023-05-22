from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=True, null=True)
    prime = models.BooleanField(default=False, blank=True, null=True)
    credit_cards = models.ManyToManyField('CreditCard')
    addresses = models.ManyToManyField('Address')

class CreditCard(models.Model):
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiration_date = models.DateField()

class Address(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
