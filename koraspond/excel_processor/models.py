from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    def __str__(self):
        return self.name
    
class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.CharField(max_length=225)
    value = models.CharField(max_length=225)

    def __str__(self):
        return self.key