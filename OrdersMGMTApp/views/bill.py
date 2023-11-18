from uuid import uuid4
from django.shortcuts import render, redirect
from OrdersMGMTApp.models import Item
from django.views import View
from OrdersMGMTApp.templatetags.cart import qty_in_cart,amt_product
from OrdersMGMTApp.models.order import Order
from django.utils.timezone import now

class Bill(View):
    def post(self,request):
        pass
    def get(self,request):
        tbl = request.session.get('tbl')
        item_ids = request.session.get(str(tbl)).keys()
        items = Item.get_items_by_ids(item_ids)
        cartid = uuid4()
        for i in items:
            order = Order(
                          item=i,
                          quantity=qty_in_cart(i, request.session),
                          cartuuid=cartid,
                          )
            print(order)
            order.place_order()
        return render(request, 'bill.html',{'products': items})



