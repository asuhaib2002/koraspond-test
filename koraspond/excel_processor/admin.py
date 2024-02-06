from django.contrib import admin
from .models import Product, ProductAttributes, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(Category)