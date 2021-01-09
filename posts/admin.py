# Django imports
from django.contrib import admin

# Models
from posts.models import Post

# Register your models here.

# Registro sencillo
# admin.site.register(Post)

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts Admin"""
    list_display = (
        'pk',
        'user',
        'title',
        'photo'
    )
    list_display_links = (
        'pk',
        'user'
    )
    list_editable = (
        'title',
        'photo'
    )
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name'
        'profile',
        'title',
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created_at',
        'updated_at',
    )
    fieldsets = (
        ('Posts', {
            'fields': (
                ('user', 'title'),),
        }),
        ('Extra info', {
            'fields': (
                ('profile', 'photo'),),
        }),
        ('Metadata', {
            'fields': (('created_at', 'updated_at'),),
        })
    )
    readonly_fields = ('created_at', 'updated_at', 'user')