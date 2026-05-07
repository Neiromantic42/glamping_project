from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'orientation', 'order', 'is_active', 'created_at']
    list_filter = ['orientation', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']

    fieldsets = (
        ('Основное', {
            'fields': ('image', 'title', 'description')
        }),
        ('Настройки', {
            'fields': ('orientation', 'order', 'is_active')
        }),
    )