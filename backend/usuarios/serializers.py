from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True, max_length=50)

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,max_length=50)
    email = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(required=True,max_length=50)
    first_name = serializers.CharField(required=True,max_length=50)
    last_name = serializers.CharField(required=True,max_length=50)
    phone = serializers.CharField(required=True, max_length=50)

class CreditCardSerializer(serializers.Serializer):
    card_number = serializers.CharField(required=True, max_length=16)
    cvv = serializers.CharField(required=True, max_length=3)
    expiration_data = serializers.DateField(required=True)

class AddressSerializer(serializers.Serializer):
    address = serializers.CharField(required=True,max_length=50)
    city = serializers.CharField(required=True,max_length=50)
    state = serializers.CharField(required=True,max_length=50)
    country = serializers.CharField(required=True,max_length=50)
    zip_code = serializers.CharField(required=True, max_length=5)

class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,max_length=50)
    email = serializers.CharField(required=True,max_length=50)
    first_name = serializers.CharField(required=True,max_length=50)
    last_name = serializers.CharField(required=True,max_length=50)
    phone = serializers.CharField(required=True, max_length=50)
    prime = serializers.BooleanField(required=True)
    credit_cards = CreditCardSerializer(many=True)
    addresses = AddressSerializer(many=True)

class ChangePasswordSerializer(serializers.Serializer):
    oldpassword = serializers.CharField(max_length=128, required=True)
    newpassword = serializers.CharField(max_length=128, required=True)

