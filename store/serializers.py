from rest_framework import serializers
from .models import Product, Category, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'category', 'unit_price',
            'sku', 'slug', 'inventory', 'last_update', 'images'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'items']