from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from garage.serializers import CategorySerializer
from garage.serializers import BrandSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.object.all()
    serializer_class = CategorySerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.object.all()
    serializer_class = BrandSerializer
