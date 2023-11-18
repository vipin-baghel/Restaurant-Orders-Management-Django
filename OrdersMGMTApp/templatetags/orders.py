from django import template

register = template.Library()

@register.filter(name='amt_calc')
def amt_calc(qty, item_price):
    return qty * item_price



    