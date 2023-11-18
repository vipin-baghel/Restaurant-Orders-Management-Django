from django.db import models
from .ItemCategory import ItemCategory


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, default=1)

    def get_items_by_ids(id_list: list):
        return Item.objects.filter(id__in=id_list)

    def get_all_items():
        return Item.objects.all()

    def get_items_by_categoryid(c_id):
        if c_id:
            return Item.objects.filter(category=c_id)
        else:
            return Item.get_all_items()

    def __str__(self):
        return self.name
