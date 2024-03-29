"""Models of store."""
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class ProductCategory(models.Model):
    """Model of items category."""
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model of product - item of store."""
    name = models.CharField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'Product: {self.name} | Category: {self.category}'


class User(AbstractUser):
    """Model of user."""
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class CartQueryset(models.QuerySet):
    def total_sum(self):
        return sum(cart.sum() for cart in self.filter())

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    """Model of user's cart."""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQueryset.as_manager()

    def sum(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'Cart for {self.user.email} | Product: {self.product.name}'


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def send_email_verification(self):
        link = reverse('u:email_verification', kwargs={
            'email': self.user.email,
            'code': self.code,
        })
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Email verification for {self.user.username}'
        message = f'''
            To verify your email on Store follow this link {verification_link}
        '''
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[
                self.user.email,
            ],
            fail_silently=False,
        )

    def is_expired(self):
        return now() >= self.expiration

    def __str__(self) -> str:
        return f'EmailVerification object for {self.user.email}'


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Created'),
        (PAID, 'Paid'),
        (ON_WAY, 'Deliver'),
        (DELIVERED, 'Delivered'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    cart_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'''
            Order #{self.id}. {self.first_name} {self.last_name}
            | {self.created}
        '''
