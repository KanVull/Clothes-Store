from django.contrib import admin

from core.models import (
    Product,
    ProductCategory,
    User,
    Cart,
    EmailVerification,
)

admin.site.register(ProductCategory)


class CartAdmin(admin.TabularInline):
    model = Cart
    fields = (
        'product',
        'quantity',
        'created_timestamp',
    )
    readonly_fields = ('created_timestamp',)
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'category',
        'quantity',
    )
    fields = (
        'name',
        'description',
        (
            'price',
            'quantity',
        ),
        'image',
        'category',
    )
    readonly_fields = (
        'quantity',
    )
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('username',)
    inlines = (CartAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration',)
    fields = ('code', 'user', 'expiration', 'created',)
    readonly_fields = ('created',)
