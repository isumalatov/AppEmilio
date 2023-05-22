from rest_framework import serializers
from .models import Product, Shoe, Accessory, Watch, Belt, Bag, Cap


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = '__all__'


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'


class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'


class BeltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belt
        fields = '__all__'


class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = '__all__'


class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cap
        fields = '__all__'
