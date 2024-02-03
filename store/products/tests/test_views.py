from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from core.models import Product, ProductCategory


class TestView(TestCase):
    fixtures = [
        'categories.json',
        'products.json',
    ]

    def setUp(self):
        self.products = Product.objects.all()

    def test_indexview_opening(self):
        path = reverse('index')
        response = self.client.get(path)

        self._common_tests(response, 'Store', ['products/index.html'])

    def test_productview_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_tests(response, 'Store - Catalog', [
            'products/products.html',
            'products/base.html',
        ])
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products[:3])
        )

    def test_productview_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse(
            'products:category',
            kwargs={'category_id': category.id}
        )
        response = self.client.get(path)

        self._common_tests(response, 'Store - Catalog', [
            'products/products.html',
            'products/base.html',
        ])
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id))
        )

    def _common_tests(self, response, title, templates):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], title)
        for template in templates:
            self.assertTemplateUsed(response, template)
