from django.core.validators import RegexValidator
from django.db import models
from glamping.models import Glamping
from django.utils.translation import gettext_lazy as _ # Позволяет переводить текст интерфейса на другие языки
from django.core.validators import MinValueValidator, MaxValueValidator

class Booking(models.Model):
    """
    Модель Booking представляет собой одну запись в бд

    О бронировании глемпинга
    """
    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')

    class Status(models.TextChoices):
        """
        Варианты статусов бронирования глэмпинга.

        - PENDING: Заявка создана, но еще не обработана менеджером.
        - CONFIRMED: Бронирование подтверждено, даты зарезервированы.
        - CANCELLED: Бронирование отменено пользователем или системой.
        - COMPLETED: Гость успешно выехал, услуга оказана.
        """
        PENDING = 'pending', 'В ожидании'
        CONFIRMED = 'confirmed', 'Подтверждено'
        CANCELLED = 'cancelled', 'Отменено'
        COMPLETED = 'completed', 'Завершено'

    glamping = models.ForeignKey(
        Glamping,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name="Глемпинг"
    ) # Связь много бронирований → один глэмпинг(многие к одному)

    name = models.CharField(
        max_length=30,
        unique=False,
        verbose_name="Имя пользователя",
        null=False,
        blank=False
    )
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9\s\-\(\)]{7,20}$',
                message="Введите корректный номер телефона"
            )
        ],
        verbose_name="Телефон клиента",
        blank=False,
        null=False,
        unique=False,
    )
    email = models.EmailField(
        verbose_name="Email клиента",
        blank=False,
        null=False,
    )
    check_in_date = models.DateField(
        verbose_name="Дата заезда гостей глемпинга",
        blank=False,
        null=False
    )
    check_out_date = models.DateField(
        blank=False,
        null=False,
        verbose_name="Дата выезда клиентов глемпинга"
    )
    guests_count = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        verbose_name="Количество гостей",
        blank=False,
        null=False,
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания брони"
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Статус бронирования"
    )

    def __str__(self):
        return f"{self.name} ({self.check_in_date} - {self.check_out_date})"
