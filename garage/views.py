from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from garage.models import Category, Brand, Acessory, Color, Vehicle

from garage.serializers import CategorySerializer, BrandSerializer, AcessorySerializer, ColorSerializer, VehicleSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class AcessoryViewSet(ModelViewSet):
    queryset = Acessory.objects.all()
    serializer_class = AcessorySerializer

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
