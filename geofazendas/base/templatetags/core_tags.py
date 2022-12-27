from django.template import Library


register = Library()


@register.simple_tag
def page_url(request, page_number):
    params = request.GET.copy()
    params['page'] = page_number
    return params.urlencode()
