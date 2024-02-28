from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema

from drfecommerce.product.models import (Product, Brand, Category)
from drfecommerce.product.serializers import (CategorySerializer,
                                              BrandSerializer,
                                              ProductSerializer
                                              )


# Create your views here.


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing Category.
    """

    serializer_class = CategorySerializer

    @extend_schema(request=CategorySerializer)
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing Brand.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @extend_schema(request=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing Product.
    """
    queryset = Product.objects.all()

    @action(
        url_path=r"category/(?P<category>[^/]+)/all",
        detail=False,
        methods=['get']
    )
    def list_products_by_category(self, request, category=None):
        serialized = ProductSerializer(self.queryset.filter(category__name=category),
                                       many=True)
        return Response(serialized.data)

    serializer_class = ProductSerializer

    @extend_schema(request=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
