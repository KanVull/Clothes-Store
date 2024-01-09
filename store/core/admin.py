from django.contrib import admin

from core.models import (
    Product,
    ProductCategory,
)

admin.site.register(Product)
admin.site.register(ProductCategory)
