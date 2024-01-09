from django.shortcuts import render


def index(request):
    """View for the main page."""
    context = {
        'title': 'Store',
        'is_promotion': False,
        'username': 'Roman',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    """View for products page."""
    context = {
        'title': 'Store - Catalog',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'card_title': 'Black hoodie with monograms adidas Originals',
                'price': 6090.00,
                'description':
                    'Soft fabric for sweatshirts. Style and comfort \
                    are a way of life.',
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'card_title': 'Blue jacket The North Face',
                'price': 23725.00,
                'description':
                    'Smooth fabric. Waterproof coating. Light and warm \
                    down filling.',
            },
            {
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'card_title': 'Brown sport oversized-top ASOS DESIGN',
                'price': 3390.00,
                'description':
                    'Plush texture material. Comfortable and soft.',
            },
        ],
    }
    return render(request, 'products/products.html', context=context)
