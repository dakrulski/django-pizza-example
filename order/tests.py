from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Pizza
from order.models import Order


class OrderTests(APITestCase):
    def test_create_order(self):
        """
        Ensure we can create an order.
        """
        url = reverse('order:create')
        data = {
            'pizza': 1,
            'size': 30,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().pizza, Pizza.objects.get(id=1))
