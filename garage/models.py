from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField (max_length=100, null=True)

    def __str__(self):
        return self.name.upper()
    
class Category(models.Model):
    description_cat = models.CharField(max_length=100)

    def __str__(self):
        return self.description_cat
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
class Acessory(models.Model):
    description_ace = models.CharField(max_length=100)

    def __str__(self):
        return self.description_ace
    
    class Meta:
        verbose_name = "Acessory"
        verbose_name_plural = "Acessories"
    
class Color(models.Model):
    description_col = models.CharField(max_length=100)

    def __str__(self):
        return self.description_col
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"
    
class Vehicle(models.Model):
    brand = models.ForeignKey(
        Brand,  on_delete=models.PROTECT, related_name = "vehicles"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name = "vehicles"
    )
    color = models.ForeignKey(
        Color, on_delete=models.PROTECT, related_name="vehicles"
    )
    year = models.IntegerField(default=0, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2,null=True)

    def __str__(self):
        return f"{self.brand} {self.category} {self.year} {self.color}"
    
    
