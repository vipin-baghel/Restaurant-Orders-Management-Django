from django.db import models

class ItemCategory(models.Model):
    name = models.CharField(max_length=50)

    def get_all_categories():
        return ItemCategory.objects.all()


    def __str__(self):
        return self.name

