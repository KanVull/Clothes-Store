from typing import Any
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from common.views import TitleMixin
from core.models import Cart, User, EmailVerification
from users.forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserProfileForm,
)


class UserLoginView(TitleMixin, LoginView):
    """View for login.html page."""
    title = 'Store - Sign in'
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    """ View for registration a new user."""
    title = 'Store - Sign up'
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('u:login')
    success_message = 'Success registration!'


class UserProfileView(TitleMixin, UpdateView):
    """View for profile.html page."""
    title = 'Store - Account'
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self) -> str:
        return reverse_lazy('u:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context.update({
            'carts': Cart.objects.filter(user=self.object)
        })
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Email Verification'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        user = User.objects.get(email=kwargs.get('email'))
        email_vrf = EmailVerification.objects.filter(
            user=user,
            code=code,
        )
        if email_vrf.exists() and not email_vrf.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(
                request, *args, **kwargs
            )
        else:
            HttpResponseRedirect(reverse('index'))
