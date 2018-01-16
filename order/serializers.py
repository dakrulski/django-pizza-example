from rest_framework import serializers
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        extra_kwargs = {'size': {'required': True}}
        fields = ('id', 'pizza', 'size', 'customer_name', 'customer_address', 'price')
