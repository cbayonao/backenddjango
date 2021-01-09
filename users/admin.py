"""User Admin Class"""
# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Models
from users.models import Profile

# Register your models here.

# Registro sencillo
# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile admin
    """
    # Me permite organizar la vista de como se muestra los perfiles de usuario
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture'
        )
    list_display_links = (
        'pk',
        'user'
        )
    list_editable = (
        'phone_number',
        'website',
        'picture'
        )
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
        )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created_at',
        'updated_at'
        )
    # Estructura para mostrar los datos del las clases
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')),
        }),
        ('Metadata', {
            'fields': (('created_at', 'updated_at'),),
        })
    )
    # Campos que son solo de lectura
    readonly_fields = ('created_at', 'updated_at', 'user')

class ProfileInline(admin.StackedInline):
    """
    Profile inline admin for users :)
    """
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """
    Add profile admin to base user admin
    """
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)