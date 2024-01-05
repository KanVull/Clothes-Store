from django.shortcuts import render


def index(request):
    """View for the main page."""
    return render(request, 'products/index.html')


def products(request):
    """View for products page."""
    return render(request, 'products/products.html')
