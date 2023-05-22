from rest_framework import serializers
from carritos.serializers import CartSerializer
from usuarios.serializers import AddressSerializer, CreditCardSerializer
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    shipping_address = AddressSerializer()
    credit_card = CreditCardSerializer()

    class Meta:
        model = Order
        fields = ['id', 'user', 'cart', 'order_date', 'total', 'status', 'shipping_address', 'credit_card']
