from django.urls import path

from products.views import ProductListView, cart_add, cart_remove

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('p/<int:page>', ProductListView.as_view(), name='p'),
    path(
        'category/<int:category_id>',
        ProductListView.as_view(),
        name='category',
    ),
    path('carts/add/<int:product_id>/', cart_add, name='cart_add'),
    path('carts/remove/<int:cart_id>/', cart_remove, name='cart_remove'),
]
