from rest_framework import generics
from rest_framework import mixins
from order.models import Order
from order.serializers import OrderSerializer


# The Task was just to create, update or delete an order. If you just want to do that, use this class instead of
# the activ OrderModify-Class. But I find it better to test and work with this simple API, if you have a GET-Method so
# I used a RetrieveUpdateDestroyAPIView.
#
# class OrderModify(mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   generics.GenericAPIView):
#     """
#     Update or delete an order
#     """
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class OrderModify(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return an order by the given order id.

    put:
    Update a complete order by the given order id.

    patch:
    Update a partial order by the given order id.

    delete:
    Delete an order by the given order id.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderCreate(generics.CreateAPIView):
    """
    post:
    Create a new order.
    """
    model = Order
    serializer_class = OrderSerializer


class OrderList(generics.ListAPIView):
    """
    get:
    Return a list of all the existing orders by a customer.
    """
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer = self.kwargs['customer']
        queryset = self.model.objects.filter(customer_name=customer)
        return queryset
