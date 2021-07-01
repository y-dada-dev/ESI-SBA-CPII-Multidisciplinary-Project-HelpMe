from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username',)
    list_filter = ('username', 'location',)
    list_display = ('email', 'username', 'location', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'is_staff', 'is_admin')}),
        ('Permissions', {'fields': ('groups', 'user_permissions',)}),
    )


admin.site.register(Users, UserAdminConfig)
