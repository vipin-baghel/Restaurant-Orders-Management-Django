from django.shortcuts import render, redirect
from OrdersMGMTApp.models import Item
from django.views import View

class Order_token(View):
    def post(self,request):
        pass
    def get(self,request):
        tbl = request.session.get('tbl')
        item_ids = request.session.get(str(tbl)).keys()
        items = Item.get_items_by_ids(item_ids)
        return render(request, 'order_token.html',{'products': items, 'tbl':tbl })