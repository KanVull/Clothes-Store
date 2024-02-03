from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):

    def test_indexview_opening(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store')
