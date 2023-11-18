from django import template

register = template.Library()


@register.filter(name='qty_in_cart')
def qty_in_cart(product, session):
    tbl = session['tbl']
    cart = session[str(tbl)]
    quantity = cart.get(str(product.id))
    return int(quantity)


@register.filter(name='amt_product')
def amt_product(product, session):
    return product.price * qty_in_cart(product, session)


@register.filter(name='total_cart_amt')
def total_cart_amount(products, session):
    sum = 0
    for p in products:
        sum += amt_product(p, session)
    return sum

@register.filter(name='discount')
def discount(products, session):
    total_amt = total_cart_amount(products, session)
    return total_amt * 0.10

@register.filter(name='gst')
def gst(products, session):
    total_amt = total_cart_amount(products, session)
    return total_amt * 0.18

@register.filter(name='payable')
def payable(products, session):
    return total_cart_amount(products, session) - discount(products, session) + gst(products, session)
    
    