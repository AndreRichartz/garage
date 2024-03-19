from django.contrib import admin

# Register your models here.

from garage.models import Brand, Category, Acessory, Color

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Acessory)
admin.site.register(Color)
