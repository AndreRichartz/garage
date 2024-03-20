from rest_framework.serializers import ModelSerializer

from garage.models import Brand, Category 

class CategorySerializer:
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer:
    model = Brand
    fields = "__all_"