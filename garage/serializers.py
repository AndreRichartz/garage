from rest_framework.serializers import ModelSerializer

from garage.models import Brand, Category, Acessory, Color, Vehicle

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class AcessorySerializer(ModelSerializer):
    class Meta:
        model = Acessory
        fields = "__all__"

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"