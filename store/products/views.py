from django.shortcuts import render

from core.models import (
    Product,
    ProductCategory,
)


def index(request):
    """View for the main page."""
    context = {
        'title': 'Store',
        'is_promotion': False,
        'username': 'Roman',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    """View for products page."""
    context = {
        'title': 'Store - Catalog',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)
