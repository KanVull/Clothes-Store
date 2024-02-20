from django import forms

from core.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'first_name',
            'last_name',
            'email',
            'address',
        )
