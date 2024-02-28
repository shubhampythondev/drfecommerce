from rest_framework import serializers
from drfecommerce.product.models import (Product,
                                         Brand,
                                         Category,
                                         ProductLine,
                                         )


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "brand_name",
            "category_name",
        )


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
