from django.template import Library

register = Library()

@register.filter
def placeholder(field):
    print(field)