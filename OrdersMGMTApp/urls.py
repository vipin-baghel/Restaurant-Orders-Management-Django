from django.urls import path

from OrdersMGMTApp.views.order_token import Order_token

from .views.bill import Bill
from .views.home import Home
from .views.cart import Cart
from .views.orders import Orders

urlpatterns= [
    path('', Home.as_view(), name='homepage'),
    path('cart', Cart.as_view(), name='cart'),
    path('bill', Bill.as_view(), name='bill'),
    path('orders', Orders.as_view(), name='orders'),
    path('order_token', Order_token.as_view(), name='order_token'),
]