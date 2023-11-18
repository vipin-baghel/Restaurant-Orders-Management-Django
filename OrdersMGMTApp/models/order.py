import uuid
from django.utils.timezone import now
from django.db import models

from .Customer import Customer
from .Item import Item

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.IntegerField(default=0)
    cartuuid = models.UUIDField(default=None, editable=False, unique=False,null=True)

    def place_order(self):
        self.save()

    def get_all_orders():
        return Order.objects.order_by('-datetime')

    def get_orders_by_cid(cid):
        return Order.objects.filter(customer=cid).order_by('-datetime')
