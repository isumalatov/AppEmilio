from django.db import models
from usuarios.models import UserProfile
from productos.models import Product


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


