from django.contrib import admin
from .models import CinemaBooking


@admin.register(CinemaBooking)
class CinemaBookingAdmin(admin.ModelAdmin):
    """
    Администрирование заказов сеансов кинотеатра
    """

    list_display = ('name', 'movie_name', 'session_date', 'session_time', 'status', 'created_at')
    list_filter = ('status', 'session_date', 'created_at')
    search_fields = ('name', 'phone', 'email', 'movie_name')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Клиент', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Заказ фильма', {
            'fields': ('movie_name', 'session_date', 'session_time')
        }),
        ('Пожелания', {
            'fields': ('comments',),
            'classes': ('wide',)
        }),
        ('Статус', {
            'fields': ('status',)
        }),
        ('Служебная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    date_hierarchy = 'session_date'