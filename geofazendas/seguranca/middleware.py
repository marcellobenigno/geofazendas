import datetime as dt

from django.utils.deprecation import MiddlewareMixin


class LastAccessMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            request.user.last_access = dt.datetime.now()
            request.user.save()


class DisableCSRF(MiddlewareMixin):

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
