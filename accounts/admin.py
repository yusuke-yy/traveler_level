from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from accounts import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email','username']
    fieldsets = (
        (None, {'fields': ('email','password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2')
        }),
    )

admin.site.register(models.CustomUser, UserAdmin)
admin.site.register(models.Profile)
admin.site.register(models.Message)


