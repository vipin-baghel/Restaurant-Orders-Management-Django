from django.shortcuts import render, redirect
from django.views import View
from OrdersMGMTApp.models.ItemCategory import ItemCategory
from OrdersMGMTApp.models.Item import Item

class Home(View):
    def post(self, request):
        print("Inside Home, handling post req")
        pid = request.POST.get('pid')
        rem = request.POST.get('rem')
        tbl = request.session.get('tbl')
        tblpost = request.POST.get('tbl')
        billed = request.POST.get('billed')

        if billed:
            request.session[tbl] = {}
            return redirect('homepage')

        if tblpost:
            request.session['tbl'] = tblpost
            return redirect('homepage')
        
        cart = request.session.get(str(tbl))

        if cart:
            quantity = cart.get(pid)
            if rem:
                if quantity == 1:
                    cart.pop(pid)
                else:
                    cart[pid] = quantity - 1
            else:
                if quantity is None:
                    cart[pid] = 1
                else:
                    cart[pid] = quantity + 1
        else:
            cart = {}
            cart[pid] = 1

        request.session[tbl] = cart
        return redirect('homepage')

    def get(self, request):
        print("Inside home, handling get req, session :- ")
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))

        if not request.session.get('tbl'):
            request.session['tbl'] =  1

        categories = ItemCategory.get_all_categories()
        c_id = request.GET.get('category')
        items = Item.get_items_by_categoryid(c_id)
        return render(request, 'index.html', {'products': items, 'categories': categories})




