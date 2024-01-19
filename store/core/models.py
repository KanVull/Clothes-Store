"""Models of store."""
from django.db import models
from django.contrib.auth.models import AbstractUser

class ProductCategory(models.Model):
    """Model of items category."""
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model of product - item of store."""
    name = models.CharField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'Product: {self.name} | Category: {self.category}'


class User(AbstractUser):
    """Model of user."""
    image = models.ImageField(upload_to='users_images', null=True, blank=True)