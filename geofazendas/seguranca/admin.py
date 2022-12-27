from django.contrib import admin

from geofazendas.seguranca.models import Usuario, SMS
from geofazendas.seguranca.forms import UserAdminForm


@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):

    list_display = ['identificador', 'nome', 'is_active', 'criado', 'modificado']
    search_fields = ['nome', 'email', 'telefone']
    exclude = ['password']
    fieldsets = (
        (None, {
            'fields': (
                'identificador', 'nome', 'email', 'is_active',
            )
        }), (
            'Permissões', {
                'fields': (
                    'is_staff', 'is_superuser', 'new_password', 'groups', 'user_permissions',
                    'sindicato'
                ),
            }
        ), (
            'Contato', {
                'fields': ('telefone', 'municipio')
            }
        )
    )
    form = UserAdminForm
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(SMS)
class SMSAdmin(admin.ModelAdmin):

    list_display = ['telefone', 'codigo', 'criado']
    search_fields = ['telefone']
