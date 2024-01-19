from django.shortcuts import render


def login(request):
    """View for login.html page."""
    context = {
        'title': 'Store - Sign In',
    }
    return render(request, 'users/login.html', context=context)


def register(request):
    """View for register.html page."""
    context = {
        'title': 'Store - Sign Up',
    }
    return render(request, 'users/register.html', context=context)


def profile(request):
    """View for profile.html page."""
    return render(request, 'users/profile.html')
