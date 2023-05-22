from django.db import models
from usuarios.models import UserProfile
from carritos.models import Cart
from usuarios.models import Address, CreditCard

class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("shipped", "Shipped"), ("delivered", "Delivered")], default="pending")
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
