from django.contrib import admin
from .models import Profile
from django.utils.html import format_html


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Админка профиля пользователя
    """

    list_display = (
        "id",
        "user",
        "display_name",
        "phone",
        "avatar_preview",
        "created_at",
    )

    # 🔍 поиск по пользователю и имени
    search_fields = (
        "user__username",
        "display_name",
        "phone",
    )

    # 🎯 фильтры справа
    list_filter = (
        "created_at",
    )

    # ✏️ редактирование прямо в списке
    list_editable = (
        "display_name",
        "phone",
    )

    # 📌 кликабельное поле (открывает объект)
    list_display_links = (
        "id",
    )

    # 🧠 сортировка
    ordering = ("-created_at",)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />',
                obj.avatar.url
            )
        return "-"

    avatar_preview.short_description = "Avatar"