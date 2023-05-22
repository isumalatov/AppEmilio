from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='products/')
    brand = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    category = models.CharField(max_length=50)