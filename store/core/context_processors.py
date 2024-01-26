from core.models import Cart


def carts(request):
    user = request.user
    if user.is_authenticated:
        carts = Cart.objects.filter(user=user)
    else:
        carts = []

    return {'carts': carts, }
