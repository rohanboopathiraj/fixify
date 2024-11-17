from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FixifyUser


class FixifyUserAdmin(UserAdmin):
    model = FixifyUser


admin.site.register(FixifyUser, FixifyUserAdmin)
