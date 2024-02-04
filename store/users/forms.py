"""Forms for users."""
from typing import Any

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from core.models import User
from users.tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    """Form for user signing In."""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Password',
    }))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class UserRegistrationForm(UserCreationForm):
    """Form for register a new user."""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': "First name",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': "Last name",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'aria-describedby': 'usernameHelp',
        'placeholder': 'Username',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'aria-describedby': 'emailHelp',
        'placeholder': 'Email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Confirm password',
    }))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True) -> Any:
        user = super(UserRegistrationForm, self).save(commit)
        send_email_verification.delay(user.id)
        return user


class UserProfileForm(UserChangeForm):
    """Form to change user information."""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }),
        required=False,
    )
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'aria-describedby': 'usernameHelp',
        'readonly': True,
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'aria-describedby': 'emailHelp',
        'readonly': True,
    }))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
        )
