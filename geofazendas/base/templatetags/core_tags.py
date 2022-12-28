from django.conf import settings
from django.template import Library

register = Library()


@register.simple_tag
def page_url(request, page_number):
    params = request.GET.copy()
    params['page'] = page_number
    return params.urlencode()


@register.simple_tag
def get_settings(value, arg=''):
    return getattr(settings, value, arg)
