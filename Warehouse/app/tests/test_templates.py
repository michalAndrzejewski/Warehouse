from django.test import TestCase
from django.urls import reverse


class TemplateTest(TestCase):
    def test_template_product(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


