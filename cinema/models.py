from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator


class CinemaBooking(models.Model):
    """
    Модель для заказов премиум сеансов в кинотеатре
    """

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ сеанса кинотеатра'
        verbose_name_plural = 'Заказы сеансов кинотеатра'

    # Информация о клиенте
    name = models.CharField(
        max_length=100,
        verbose_name='Имя клиента'
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Email'
    )

    # Информация о фильме и сеансе
    movie_name = models.CharField(
        max_length=200,
        verbose_name='Название фильма'
    )

    session_date = models.DateField(
        verbose_name='Дата сеанса'
    )

    session_time = models.TimeField(
        verbose_name='Время начала сеанса'
    )

    # Комментарии и пожелания
    comments = models.TextField(
        max_length=2000,
        verbose_name='Пожелания и комментарии',
        validators=[MinLengthValidator(10)]
    )

    # Статус заказа
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('confirmed', 'Подтвержден'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменен'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )

    # Служебные поля
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заказа'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего обновления'
    )

    def __str__(self):
        return f"Заказ фильма '{self.movie_name}' от {self.name} на {self.session_date}"

    class Admin:
        list_display = ('name', 'movie_name', 'session_date', 'status', 'created_at')
        list_filter = ('status', 'session_date', 'created_at')
        search_fields = ('name', 'movie_name', 'phone')