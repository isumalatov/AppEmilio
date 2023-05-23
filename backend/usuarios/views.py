from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from usuarios.serializers import (
    UserLoginSerializer,
    UserRegisterSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
    CreditCardSerializer,
    AddressSerializer,
)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from usuarios.models import UserProfile, CreditCard, Address


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        else:
            return Response({"error": "Wrong Credentials"}, status=400)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        first_name = serializer.validated_data["first_name"]
        last_name = serializer.validated_data["last_name"]
        phone = serializer.validated_data["phone"]
        """ i need to save the phone number in the user profile """
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        UserProfile.objects.create(user=user, phone=phone)
        return Response({"message": "User created successfully"}, status=201)


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        Token.objects.filter(user=request.user).delete()
        return Response({"message": "Logout successfully"}, status=200)


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        old_password = serializer.validated_data["old_password"]
        new_password = serializer.validated_data["new_password"]
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password changed successfully"}, status=200)
        else:
            return Response({"error": "Wrong password"}, status=400)


class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=200)


class UpdateUserProfileView(APIView):
    def post(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        user.username = serializer.validated_data["username"]
        user.email = serializer.validated_data["email"]
        user.first_name = serializer.validated_data["first_name"]
        user.last_name = serializer.validated_data["last_name"]
        profile.phone = serializer.validated_data["phone"]
        user.save()
        profile.save()
        return Response({"message": "User profile updated successfully"}, status=200)


class CreditCardView(APIView):
    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        credit_cards = profile.credit_cards.all()
        serializer = CreditCardSerializer(credit_cards, many=True)
        return Response(serializer.data, status=200)


class AddCreditCardView(APIView):
    def post(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        serializer = CreditCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile.credit_cards.create(
            card_number=serializer.validated_data["card_number"],
            card_holder=serializer.validated_data["card_holder"],
            expiration_date=serializer.validated_data["expiration_date"],
            cvv=serializer.validated_data["cvv"],
        )
        return Response({"message": "Credit card added successfully"}, status=201)


class DeleteCreditCardView(APIView):
    def post(self, request, id):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        credit_card = profile.credit_cards.get(id=id)
        credit_card.delete()
        return Response({"message": "Credit card deleted successfully"}, status=200)


class UpdateCreditCardView(APIView):
    def post(self, request, id):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        credit_card = profile.credit_cards.get(id=id)
        serializer = CreditCardSerializer(credit_card, data=request.data)
        serializer.is_valid(raise_exception=True)
        credit_card.card_number = serializer.validated_data["card_number"]
        credit_card.card_holder = serializer.validated_data["card_holder"]
        credit_card.expiration_date = serializer.validated_data["expiration_date"]
        credit_card.cvv = serializer.validated_data["cvv"]
        credit_card.save()
        return Response({"message": "Credit card updated successfully"}, status=200)


class AddresView(APIView):
    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        addresses = profile.addresses.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=200)


class AddAddressView(APIView):
    def post(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile.addresses.create(
            street=serializer.validated_data["street"],
            number=serializer.validated_data["number"],
            city=serializer.validated_data["city"],
            state=serializer.validated_data["state"],
            country=serializer.validated_data["country"],
            zip_code=serializer.validated_data["zip_code"],
        )
        return Response({"message": "Address added successfully"}, status=201)


class DeleteAddressView(APIView):
    def post(self, request, id):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        address = profile.addresses.get(id=id)
        address.delete()
        return Response({"message": "Address deleted successfully"}, status=200)


class UpdateAddressView(APIView):
    def post(self, request, id):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        address = profile.addresses.get(id=id)
        serializer = AddressSerializer(address, data=request.data)
        serializer.is_valid(raise_exception=True)
        address.street = serializer.validated_data["street"]
        address.number = serializer.validated_data["number"]
        address.city = serializer.validated_data["city"]
        address.state = serializer.validated_data["state"]
        address.country = serializer.validated_data["country"]
        address.zip_code = serializer.validated_data["zip_code"]
        address.save()
        return Response({"message": "Address updated successfully"}, status=200)
