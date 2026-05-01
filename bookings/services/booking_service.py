from bookings.models import Booking
from bookings.services.notification_service import notify_owner_new_booking
import logging


logger = logging.getLogger(__name__)


def is_dates_available(glamping, check_in, check_out):
    """
    Функция для поиска пересечений бронирований

    Если пересечение найдено, фун-я вернет True иначе False
    """
    # Ищем существующие бронирования, которые могут помешать новой записи
    return not Booking.objects.filter(
        glamping=glamping, # Только для выбранного домика/глэмпинга
        status__in=["pending", "confirmed"], # Только активные брони (не отмененные)
        check_in_date__lt=check_out, # Старая бронь начинается раньше, чем вы уедете
        check_out_date__gt=check_in # Старая бронь заканчивается позже, чем вы приедете
    ).exists() # Если таких записей НЕТ, вернет True (свободно)


def create_booking(form, glamping):
    """
    Функция создает запись о бронировании в бд Booking
    """
    # Создаем объект бронирования из данных формы, но не записываем в БД (ждем дозаполнения)
    booking = form.save(commit=False)
    # Привязываем конкретный глэмпинг, который выбрал пользователь
    booking.glamping = glamping
    # Устанавливаем начальный статус (бронь ожидает оплаты или подтверждения)
    booking.status = "pending"
    # Сохраняем уже полностью заполненный объект в базу данных
    booking.save()
    # Возвращаем созданный объект бронирования для дальнейшего использования (например, оплаты)
    try: # Отправляем сообщение на почту арендодателю о попытке бронирования
        notify_owner_new_booking(booking)
    except Exception as e:
        logger.error(f"Ошибка отправки email владельцу: {e}")
    return booking

