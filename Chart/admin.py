from django.contrib import admin
from .models import UserType, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'name', 'user_type' )
    search_fields = ('name', )
    ordering = ('email',)
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Personal', {'fields': ('mobile', 'user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'is_staff', 'is_active', 'user_type')}
        ),
    )

    filter_horizontal= ()

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserType)
