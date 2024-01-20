from django.shortcuts import render, HttpResponseRedirect

from core.models import (
    Product,
    ProductCategory,
    Cart,
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


def cart_add(request, product_id):
    """Controller to add product to user cart."""
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    """Controller to remove object from cart."""
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
