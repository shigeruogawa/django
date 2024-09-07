from django import template
from wcwidth import wcswidth

register = template.Library()

@register.filter
def wcwidth(value):
    return wcswidth(value)
