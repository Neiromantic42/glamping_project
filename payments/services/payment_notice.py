from django.core.mail import send_mail
from django.conf import settings

STATUS_RU = {
    "pending": "Ожидает подтверждения",
    "confirmed": "Подтверждена",
    "canceled": "Отменена",
}

def notify_owner_payment_attempt(booking, nights, total_price, prepayment):
    admin_url = f"http://127.0.0.1:8000/admin/bookings/booking/{booking.id}/change/"

    subject = "Пользователь нажал 'Я оплатил'"

    message = f"""
    Пользователь перешёл к оплате и нажал кнопку оплатил(подтвердил оплату):

    Имя: {booking.name}
    Телефон: {booking.phone}
    Email: {booking.email}

    Заезд: {booking.check_in_date}
    Выезд: {booking.check_out_date}

    Гостей: {booking.guests_count}
    Ночей: {nights}
    Предоплата: {prepayment}
    Общая стоимость: {total_price} руб.
    Остаток после предоплаты: {total_price - prepayment} руб.
    

    Статус сейчас: {STATUS_RU.get(booking.status, booking.status)}
    

    Админка:
    {admin_url}

    ВАЖНО: проверь поступление оплаты вручную.
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.OWNER_EMAIL],
        fail_silently=False,
    )