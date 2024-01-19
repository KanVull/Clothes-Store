from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserProfileForm,
)


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


def register(request):
    """View for register.html page."""
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Congrats. Account was created successfully"
            )
            return HttpResponseRedirect(reverse('u:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Store - Sign Up',
        'form': form,
    }
    return render(request, 'users/register.html', context=context)


def profile(request):
    """View for profile.html page."""
    if request.method == 'POST':
        form = UserProfileForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('u:profile'))

    form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Store - Profile',
        'form': form,
    }
    return render(request, 'users/profile.html', context=context)


def logout(request):
    """View to logout a user."""
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
