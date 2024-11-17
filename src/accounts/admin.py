from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FixifyUser


class FixifyUserAdmin(UserAdmin):
    model = FixifyUser
    list_display = ['email', 'first_name',
                    'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']  # Set ordering by email instead of username

    # Update fieldsets to remove references to 'username'
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Update add_fieldsets to remove references to 'username'
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


# Register your custom user model
admin.site.register(FixifyUser, FixifyUserAdmin)
