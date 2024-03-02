from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from members.models import Member

class UserAdminConfig(UserAdmin):
  
    model = Member
    search_fields = ('user_name', 'email', 'first_name',)
    list_filter = ('user_name', 'email', 'first_name', 'is_active', 'is_staff')
    ordering = ('user_name',)
    list_display = ('user_name', 'email', 'first_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('user_name', 'email', 'first_name', 'last_name', 'birthday', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Member, UserAdminConfig)