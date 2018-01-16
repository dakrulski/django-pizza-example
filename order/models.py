from django.db import models
from main.models import Pizza


class Order(models.Model):
    pizza = models.ForeignKey('main.Pizza', on_delete=models.PROTECT)
    size = models.IntegerField(choices=Pizza.PIZZA_SIZES, default=30, blank=False)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField(null=False, blank=False)

    @property
    def price(self):
        """ Returns the price of the order. """
        # If there are more than 2 sizes, this should be cleaned. But for this simple App it's fine.
        if self.size == 30:
            return self.pizza.price_small
        if self.size == 50:
            return self.pizza.price_big
        # default that shouldnt be nessesary
        return self.pizza.price_small
