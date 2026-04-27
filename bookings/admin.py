from django.contrib import admin
from .models import Booking



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "phone",
        "glamping",
        "check_in_date",
        "check_out_date",
        "guests_count",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
    )

    list_filter = (
        "status",
        "glamping",
        "check_in_date",
        "check_out_date",
        "created_at",
    )

    fieldsets = (
        ("Основное", {
            "fields": ("glamping", "status")
        }),
        ("Клиент", {
            "fields": ("name", "phone", "email", "guests_count")
        }),
        ("Даты бронирования", {
            "fields": ("check_in_date", "check_out_date")
        }),
        ("Служебная информация", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )

    readonly_fields = ("created_at",)