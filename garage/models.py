from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField (max_length=100, null=True)

    def __str__(self):
        return self.name.upper()
    