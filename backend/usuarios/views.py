from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from usuarios.serializers import UserLoginSerializer, UserRegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from usuarios.models import UserProfile


class LoginView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        else:
            return Response({'error': 'Wrong Credentials'}, status=400)
    
class RegisterView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        first_name = serializer.validated_data['first_name']
        last_name = serializer.validated_data['last_name']
        phone = serializer.validated_data['phone']
        """ i need to save the phone number in the user profile """
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        UserProfile.objects.create(user=user, phone=phone)
        return Response({'message': 'User created successfully'}, status=201)
    
class LogoutView(APIView):
    
        def get(self, request):
            logout(request)
            Token.objects.filter(user=request.user).delete()
            return Response({'message': 'Logout successfully'}, status=200)
