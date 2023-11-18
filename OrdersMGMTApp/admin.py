from django.contrib import admin

from .models.ItemCategory import ItemCategory
from .models.Customer import Customer
from .models.Item import Item
from .models.order import Order

class AdminOrder(admin.ModelAdmin):
    list_display = ['item', 'customer', 'quantity', 'status', 'datetime',]
    raw_id_fields = ['customer', 'item']
    search_fields = ['customer__name', 'item__name', 'status', 'datetime']
admin.site.register(Order, AdminOrder)

class AdminItem(admin.ModelAdmin):
    list_display = ['name','price','category']
    search_fields = ['name']
admin.site.register(Item, AdminItem)

class AdminItemCategory(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
admin.site.register(ItemCategory, AdminItemCategory)

class AdminCustomer(admin.ModelAdmin):
    list_display = ['name','phone']
    search_fields = ['name','phone']
admin.site.register(Customer, AdminCustomer)