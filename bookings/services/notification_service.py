from django.core.mail import send_mail
from django.conf import settings

STATUS_RU = {
    "pending": "Ожидает подтверждения",
    "confirmed": "Подтверждена",
    "canceled": "Отменена",
}


def notify_owner_new_booking(booking):
    """
    Уведомление владельца о новой заявке на бронирование
    """

    admin_url = f"http://127.0.0.1:8000/admin/bookings/booking/{booking.id}/change/"

    subject = "Новая заявка на бронирование"

    message = f"""
        Поступила новая заявка:
        
        Имя: {booking.name}
        Телефон: {booking.phone}
        Email: {booking.email}
        
        Заезд: {booking.check_in_date}
        Выезд: {booking.check_out_date}
        
        Гостей: {booking.guests_count}
        
        Статус: {STATUS_RU.get(booking.status, booking.status)}
        
        Открыть в админке:
        {admin_url}
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.OWNER_EMAIL],
        fail_silently=False,
    )
