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
    
class Acessory(models.Model):
    description_ace = models.CharField(max_length=100)

    def __str__(self):
        return self.description_ace
    
class Color(models.Model):
    description_col = models.CharField(max_length=100)

    def __str__(self):
        return self.description_col
    
    
    
