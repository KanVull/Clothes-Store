from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('u/', include('users.urls', namespace='u')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
