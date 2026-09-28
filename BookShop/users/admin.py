from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Личная информация', {'fields': ('phone_number', 'birth_date',)}),)
    list_display = ('username', 'email', 'phone_number', 'birth_date', 'is_staff')