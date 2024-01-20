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


class CartQueryset(models.QuerySet):
    def total_sum(self):
        return sum(cart.sum() for cart in self.filter())

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    """Model of user's cart."""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQueryset.as_manager()

    def sum(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'Cart for {self.user.email} | Product: {self.product.name}'
