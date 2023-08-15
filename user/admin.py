from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserManager

from .models import User

class UserAdmin(BaseUserManager):
    ordering=['id']
    list_display = ['id','username', 'password', 'is_active','is_staff', 'is_admin', 'is_superuser',]
    add_fieldsets = ((None, {"fields":('username','password1','password2')}),)
    search_fields =('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )

admin.site.register(User, UserAdmin)