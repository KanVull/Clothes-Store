from typing import Any

from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from core.models import Cart, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    """View for the main page."""
    template_name = 'products/index.html'
    title = 'Store'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data()
        context.update({
            'is_promotion': True,
            'username': 'Roman',
        })
        return context


class ProductListView(TitleMixin, ListView):
    """View for products page with category and pagination."""
    title = 'Store - Catalog'
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            return queryset.filter(category_id=category_id)

        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ProductListView, self).get_context_data()
        context.update({
            'categories': ProductCategory.objects.all(),
        })
        return context


@login_required
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


@login_required
def cart_remove(request, cart_id):
    """Controller to remove object from cart."""
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
