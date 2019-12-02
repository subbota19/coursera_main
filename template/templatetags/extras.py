from django import template
from django import template

register = template.Library()


@register.filter(name='inc')
def inc(number, increase):
    try:
        return int(number) * int(increase)
    except ValueError:
        return "Expected numbers,but your submit incorrect data "


@register.simple_tag
def division(divisor, divisible, to_int=False):
    if to_int:
        return int(float(divisor) / float(divisible))
    else:
        return float(divisor) / float(divisible)
