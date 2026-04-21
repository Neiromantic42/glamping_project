from django.contrib import admin  # Импортируем модуль админки Django
from .models import Glamping      # Импортируем вашу модель Glamping из текущей папки


@admin.register(Glamping)  # Регистрируем модель в админке с помощью декоратора
class GlampingAdmin(admin.ModelAdmin):  # Создаем класс настроек отображения модели

    # Список полей, которые будут видны в таблице со всеми объектами
    list_display = (
        "title",           # Название глэмпинга
        "location",        # Локация (район/регион)
        "price_per_night", # Цена за ночь
        "max_guests",      # Максимальное количество гостей
    )

    # Поля, по которым будет работать поиск в верхней части страницы
    search_fields = ("title", "location", "address")

    # Автоматическое заполнение slug на основе поля title при вводе текста
    prepopulated_fields = {
        "slug": ("title",)
    }

    # Группировка полей в форме редактирования для удобства (визуальные блоки)
    fieldsets = (
        ("Основная информация", {  # Название первого блока
            "fields": ("title", "description", "slug") # Поля внутри блока
        }),
        ("Локация", {  # Название блока с адресами
            "fields": ("location", "address")
        }),
        ("Цены", {  # Блок для финансовых настроек
            "fields": ("price_per_night", "deposit")
        }),
        ("Проживание", {  # Блок настроек заезда и вместимости
            "fields": ("check_in_time", "check_out_time", "max_guests")
        }),
        ("Контакты", {  # Блок с контактными данными
            "fields": ("phone", "email")
        }),
    )