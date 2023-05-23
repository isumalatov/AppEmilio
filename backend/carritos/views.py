from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer


class AllCartView(APIView):
    def get(self, request):
        carritos = Cart.objects.all()
        serializer = CartSerializer(carritos, many=True)
        return Response(serializer.data)

class CartView(APIView):
    def get(self,request,id):
        carrito = Cart.objects.get(id=id)
        serializer = CartSerializer(carrito, many=False)
        return Response(serializer.data)

class CartCreateView(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class CartUpdateView(APIView):
    def post(self, request, id):
        carrito = Cart.objects.get(id=id)
        serializer = CartSerializer(instance=carrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)