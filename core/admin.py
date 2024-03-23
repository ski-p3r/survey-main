from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # list_display = ('id', 'name', 'email', 'phone',
    #                 'user_type', 'survey', 'is_staff')
    # list_display_links = ('email', 'name')
    search_fields = ('email', 'name')
    ordering = ('-last_login',)


admin.site.register(User)
