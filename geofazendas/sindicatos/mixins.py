from django.contrib.auth.mixins import UserPassesTestMixin

from rolepermissions.checkers import has_role


class SindicatoRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return bool(
            self.request.user.is_authenticated and has_role(self.request.user, 'sindicato') \
                and self.request.user.sindicato
        )
