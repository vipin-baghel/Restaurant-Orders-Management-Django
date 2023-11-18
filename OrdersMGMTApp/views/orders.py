from django.views import View
from django.shortcuts import render, redirect

from OrdersMGMTApp.models import Order

class Orders(View):
    def post(self, request):
        pass

    def get(self, request):
        orders = Order.get_all_orders()
        print(orders)
        return render(request, 'orders.html', {'orders': orders})
