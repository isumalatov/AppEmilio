from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


class AllOrdenesView(APIView):
    def get(self, request):
        ordenes = Order.objects.all()
        serializer = OrderSerializer(ordenes, many=True)
        return Response(serializer.data)


class OrdenView(APIView):
    def get(self, request, pk):
        orden = Order.objects.get(id=pk)
        serializer = OrderSerializer(orden, many=False)
        return Response(serializer.data)


class OrdenCreateView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class OrdenUpdateView(APIView):
    def post(self, request, id):
        orden = Order.objects.get(id=id)
        serializer = OrderSerializer(instance=orden, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class OrdenDeleteView(APIView):
    def delete(self, request, id):
        orden = Order.objects.get(id=id)
        orden.delete()
        return Response({"message": "Orden eliminada correctamente"}, status=200)


class OrdenesByUserView(APIView):
    def get(self, request, id):
        ordenes = Order.objects.filter(user=id)
        serializer = OrderSerializer(ordenes, many=True)
        return Response(serializer.data)
