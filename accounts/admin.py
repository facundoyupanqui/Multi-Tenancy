from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Client Info', {'fields': ('client',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Client Info', {'fields': ('client',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
