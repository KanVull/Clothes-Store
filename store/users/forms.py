"""Forms for users."""
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from core.models import User


class UserLoginForm(AuthenticationForm):
    """Form for user signing In."""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': "Username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': "Password",
    }))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
