from django import template

register = template.Library()

def cut(value,arg):
    """
    Corta os valores de arg da string
    """

    return value.replace(arg,'')

register.filter('cut',cut)