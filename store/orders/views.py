from django.views.generic.edit import CreateView

from common.views import TitleMixin
from orders.forms import OrderForm


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    title = 'Store - Create order'
    form_class = OrderForm
