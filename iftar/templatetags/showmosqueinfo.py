from django import template
from iftar.models import Mosque

register = template.Library()


@register.inclusion_tag('layout.html')
def show_mosque_info():
    info = Mosque.objects.all()
    return {'mosque_info': 'junk'}
