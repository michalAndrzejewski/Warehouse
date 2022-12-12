from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializaer a product objects in a databbase"""
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'product_name', 'category', 'unit_price', 'units_in_stock')


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
