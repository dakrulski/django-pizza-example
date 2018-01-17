from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Pizza
from order.models import Order


class OrderTests(APITestCase):
    def setUp(self):
        Order.objects.create(pizza=Pizza.objects.get(id=1), size=30, customer_name='Test', customer_address='Nowhere')
        self.start_order_count = 1

    def test_create_order(self):
        """
        Ensure we can create an order.
        """
        url = reverse('order:create')
        data = {
            'pizza': 2,
            'size': 30,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), self.start_order_count + 1)
        self.assertEqual(Order.objects.get(id=2).pizza, Pizza.objects.get(id=2))

    def test_create_wrong_size_order(self):
        """
        Ensure we can't create an order with a wrong size.
        """
        url = reverse('order:create')
        data = {
            'pizza': 1,
            'size': 300,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_with_wrong_pizza(self):
        """
        Ensure we can't create an order with a pizza that doesn't exist.
        """
        url = reverse('order:create')
        data = {
            'pizza': 666,
            'size': 30,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_with_missing_pizza(self):
        """
        Ensure we can't create an order with a missing pizza.
        """
        url = reverse('order:create')
        data = {
            'size': 30,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_with_missing_size(self):
        """
        Ensure we can't create an order with the size missing.
        """
        url = reverse('order:create')
        data = {
            'pizza': 1,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_with_missing_customer_name(self):
        """
        Ensure we can't create an order with a missing customer name.
        """
        url = reverse('order:create')
        data = {
            'pizza': 1,
            'size': 30,
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_with_missing_customer_address(self):
        """
        Ensure we can't create an order with a missing customer address.
        """
        url = reverse('order:create')
        data = {
            'pizza': 1,
            'size': 30,
            'customer_name': 'John Doe'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modify_order(self):
        """
        Ensure we can modify an order.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 5,
            'size': 50,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), self.start_order_count)
        self.assertEqual(Order.objects.get(id=1).pizza, Pizza.objects.get(id=5))
        self.assertEqual(Order.objects.get(id=1).size, 50)
        self.assertEqual(Order.objects.get(id=1).customer_name, 'John Doe')
        self.assertEqual(Order.objects.get(id=1).customer_address, 'Nowhere')

    def test_modify_order_with_post(self):
        """
        Ensure we can't modify an order with POST insead of PUT.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 1,
            'size': 30,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_modify_order_with_wrong_id(self):
        """
        Ensure we can't modify an order with an ID that doesn't exist.
        """
        url = reverse('order:modify', kwargs={'pk': 9001})
        data = {
            'pizza': 1,
            'size': 30,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_modify_order_with_missing_pizza(self):
        """
        Ensure we can't modify an order with a pizza missing.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'size': 30,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modify_order_with_missing_size(self):
        """
        Ensure we can't modify an order with the size missing.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 1,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modify_order_with_missing_customer_name(self):
        """
        Ensure we can't modify an order with a missing customer name.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 1,
            'size': 30,
            'customer_address': 'Nowhere'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modify_order_with_missing_customer_address(self):
        """
        Ensure we can't modify an order with a missing customer address.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 1,
            'size': 30,
            'customer_name': 'John Doe'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modify_order_with_wrong_pizza(self):
        """
        Ensure we can't modify an order with a pizza that doesn't exist.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 666,
            'size': 50,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_modify_order_with_wrong_size(self):
        """
        Ensure we can't modify an order with a size that doesn't exist.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 1,
            'size': 9001,
            'customer_name': 'John Doe',
            'customer_address': 'Nowhere'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_order_update_pizza(self):
        """
        Ensure we can patch an order with a different pizza.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 5
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), self.start_order_count)
        self.assertEqual(Order.objects.get(id=1).pizza, Pizza.objects.get(id=5))
        self.assertEqual(Order.objects.get(id=1).size, 30)
        self.assertEqual(Order.objects.get(id=1).customer_name, 'Test')
        self.assertEqual(Order.objects.get(id=1).customer_address, 'Nowhere')

    def test_patch_order_update_size(self):
        """
        Ensure we can patch an order with a different size.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'size': 50
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), self.start_order_count)
        self.assertEqual(Order.objects.get(id=1).pizza, Pizza.objects.get(id=1))
        self.assertEqual(Order.objects.get(id=1).size, 50)
        self.assertEqual(Order.objects.get(id=1).customer_name, 'Test')
        self.assertEqual(Order.objects.get(id=1).customer_address, 'Nowhere')

    def test_patch_order_update_customer_name(self):
        """
        Ensure we can patch an order with a different customer name.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'customer_name': 'Max Mustermann'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), self.start_order_count)
        self.assertEqual(Order.objects.get(id=1).pizza, Pizza.objects.get(id=1))
        self.assertEqual(Order.objects.get(id=1).size, 30)
        self.assertEqual(Order.objects.get(id=1).customer_name, 'Max Mustermann')
        self.assertEqual(Order.objects.get(id=1).customer_address, 'Nowhere')

    def test_patch_order_update_customer_address(self):
        """
        Ensure we can patch an order with a different customer address.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'customer_address': 'Behind Nowhere'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), self.start_order_count)
        self.assertEqual(Order.objects.get(id=1).pizza, Pizza.objects.get(id=1))
        self.assertEqual(Order.objects.get(id=1).size, 30)
        self.assertEqual(Order.objects.get(id=1).customer_name, 'Test')
        self.assertEqual(Order.objects.get(id=1).customer_address, 'Behind Nowhere')

    def test_patch_order_with_wrong_id(self):
        """
        Ensure we can't patch an order with a pizza that doesn't exist.
        """
        url = reverse('order:modify', kwargs={'pk': 9001})
        data = {
            'pizza': 1
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_order_with_wrong_pizza(self):
        """
        Ensure we can't patch an order with a pizza that doesn't exist.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'pizza': 9001
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_order_with_wrong_size(self):
        """
        Ensure we can't patch an order with a size that doesn't exist.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        data = {
            'size': 9001
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_order(self):
        """
        Ensure we can delete an order.
        """
        url = reverse('order:modify', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), self.start_order_count - 1)
        self.assertEqual(Order.objects.filter(id=1).count(), 0)

    def test_delete_order_with_wrong_id(self):
        """
        Ensure we can't delete an order that doesn't exist.
        """
        url = reverse('order:modify', kwargs={'pk': 9001})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_customer_order(self):
        """
        Ensure we can list the orders of a customer.
        """
        url = reverse('order:list', kwargs={'customer': 'Test'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Order.objects.count())
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[0]['pizza'], 1)
        self.assertEqual(response.data[0]['size'], 30)
        self.assertEqual(response.data[0]['customer_name'], 'Test')
        self.assertEqual(response.data[0]['customer_address'], 'Nowhere')
