from django.contrib import admin

from core.models import (
    Product,
    ProductCategory,
    User,
)

admin.site.register(Product)
admin.site.register(ProductCategory)

admin.site.register(User)
