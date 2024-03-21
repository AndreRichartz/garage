from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from garage.models import Category, Brand, Acessory

from garage.serializers import CategorySerializer, BrandSerializer, AcessorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class AcessoryViewSet(ModelViewSet):
    queryset = Acessory.objects.all()
    serializer_class = AcessorySerializer
