from datetime import time
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.db import models # импорт модулей для создания моделей
from django.utils.translation import gettext_lazy as _



class Glamping(models.Model):
    """
    Модель Glamping представляет собой объект недвижемости
    """
    class Meta:
        verbose_name = _('Glamping')
        verbose_name_plural = _('glampings')

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название Глемпинга, заголовок первого блока",
        null=False,
        blank=False
    )
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="продающий текст (hero-секция) под заголовком первого блока"
    )
    location = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Короткая “человеческая” геолокация"
    )
    address = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        db_index=True,
        verbose_name="Точный адрес (для карты, юридически и навигации)"
    )
    price_per_night = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        verbose_name="Цена за 1 ночь"
    )
    deposit = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        verbose_name="Залог"
    )
    check_out_time = models.TimeField(
        default=time(12, 0),
        verbose_name = "Время выселения",
    )
    check_in_time = models.TimeField(
        default=time(14, 0),
        verbose_name="Время заселения",

    )
    max_guests = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Параметр задает максимально допустимое кол-во гостей"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        verbose_name="URL (slug) Адресная ссылка",
        help_text="Используйте только латиницу, цифры и дефис. Определяет путь к странице."
    )
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9\s\-\(\)]{7,20}$',
                message="Введите корректный номер телефона"
            )
        ],
        verbose_name="Телефон владельца глемпинга/арендодателя",
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name="Email владельца",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
