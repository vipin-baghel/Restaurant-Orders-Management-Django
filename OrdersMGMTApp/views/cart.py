from django.shortcuts import render, redirect
from OrdersMGMTApp.models import Item
from django.views import View


class Cart(View):
    def post(self, request):
        print("inside cart,  handling POST req")
        pid = request.POST.get('pid')
        rem = request.POST.get('rem')
        tbl = request.session.get('tbl')
        tblpost = request.POST.get('tbl')
        cart = request.session.get(str(tbl))

        if tblpost:
            print("changing table")
            request.session['tbl'] = tblpost

        if rem:
            print("removing one object from cart")
            quantity = cart.get(pid)
            print(f"qty : {quantity}")
            if quantity == 1:
                cart.pop(pid)
            else:
                cart[pid] = quantity - 1
            
            request.session[tbl] = cart
        
        print("redirecting back to cart with get req")
        return redirect('cart')

    def get(self, request):
        print("inside cart.py,  handling GET req , session :- ")
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))

        tbl = request.session.get('tbl')

        if request.session.get(str(tbl)) is not None:
            item_ids = request.session.get(str(tbl)).keys()
            if len(item_ids) > 0:
                items = Item.get_items_by_ids(item_ids)
                return render(request, 'cart.html', {'products': items})
            else:
                return render(request, 'cart_empty.html')
        else:
            return render(request, 'cart_empty.html')
