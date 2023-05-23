from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from productos.serializers import ProductSerializer
from productos.models import Product


class AllProductosView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductoView(APIView):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductoCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Producto creado correctamente"}, status=201)
        return Response(serializer.errors, status=400)


class ProductoDeleteView(APIView):
    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"message": "Producto eliminado correctamente"}, status=200)
