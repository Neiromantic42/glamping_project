from django.contrib import admin
from .models import Review, ReviewImage
from django.utils.html import format_html




class ReviewImageInline(admin.TabularInline):
    """
    Inline для загрузки изображений к отзыву
    """
    model = ReviewImage
    extra = 1
    fields = ("image",)




@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "avatar",
        "author_display",
        "short_text",
        "rating",
        "stars_display",
        "images_count",
        "created_at",
    )

    search_fields = (
        "text",
        "user__username",
        "user__email",
        "author_name",
    )

    list_filter = (
        "rating",
        "created_at",
        "user",
    )

    fieldsets = (
        ("Автор", {
            "fields": ("user", "author_name", "author_avatar")
        }),
        ("Контент", {
            "fields": ("rating", "text")
        }),
        ("Служебное", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )

    readonly_fields = ("created_at",)

    inlines = [ReviewImageInline]

    list_display_links = ("id", "author_display")

    # -------------------------
    # Автор (user + seed логика)
    # -------------------------
    def author_display(self, obj):
        if obj.user:
            return obj.user.username
        return obj.author_name or "Аноним"

    author_display.short_description = "Автор"

    # -------------------------
    # Обрезка текста
    # -------------------------
    def short_text(self, obj):
        return obj.text[:40] + "..." if len(obj.text) > 40 else obj.text

    short_text.short_description = "Текст"

    # -------------------------
    # Звёзды
    # -------------------------
    def stars_display(self, obj):
        return "★" * obj.rating + "☆" * (5 - obj.rating)

    stars_display.short_description = "Рейтинг"

    # -------------------------
    # Аватар (user → seed → fallback)
    # -------------------------
    def avatar(self, obj):
        try:
            # 1. user avatar
            if obj.user and hasattr(obj.user, "profile") and obj.user.profile.avatar:
                return format_html(
                    '<img src="{}" width="40" height="40" style="border-radius:50%;" />',
                    obj.user.profile.avatar.url
                )

            # 2. seed avatar
            if obj.author_avatar:
                return format_html(
                    '<img src="{}" width="40" height="40" style="border-radius:50%;" />',
                    obj.author_avatar.url
                )

        except:
            pass

        return "—"

    avatar.short_description = "Аватар"

    # -------------------------
    # Кол-во фото
    # -------------------------
    def images_count(self, obj):
        return obj.images.count()

    images_count.short_description = "Фото"
