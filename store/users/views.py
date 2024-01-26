from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from core.models import Cart, User
from users.forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserProfileForm,
)


class UserLoginView(LoginView):
    """View for login.html page."""
    template_name = 'users/login.html'
    form_class = UserLoginForm


def login(request):
    """View for login.html page."""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(
                username=username,
                password=password,
            )
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Store - Sign In',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


class UserRegistrationView(CreateView):
    """ View for registration a new user."""
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('u:login')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UserRegistrationView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Store - Registration',
        })
        return context


class UserProfileView(UpdateView):
    """View for profile.html page."""
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self) -> str:
        return reverse_lazy('u:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Store - Account',
            'carts': Cart.objects.filter(user=self.object)
        })
        return context
