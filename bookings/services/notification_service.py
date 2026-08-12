from django.core.mail import send_mail
from django.conf import settings

STATUS_RU = {
    "pending": "Ожидает подтверждения",
    "confirmed": "Подтверждена",
    "canceled": "Отменена",
}



def notify_owner_new_booking(booking, cost):
    """
    Уведомление владельца о новой заявке на бронирование
    """

    admin_url = f"https://kama-glamping.ru/admin/bookings/booking/{booking.id}/change/"

    subject = "Новая заявка на бронирование"

    message = f"""
        Поступила новая заявка:
        
        Имя: {booking.name}
        Телефон: {booking.phone}
        Email: {booking.email}
        
        Заезд: {booking.check_in_date}
        Выезд: {booking.check_out_date}
        Ночей: {cost["nights"]}
        
        Гостей: {booking.guests_count}
        Кол-во дополнительно оплачиваемых гостей: {cost["extra_guests_count"]}
        Стоимость дополнительно оплачиваемых гостей: {cost["guest_fee"]} руб.
        
        Общая стоимость: {cost["total_price"]}
        Предоплата: {cost["prepayment"]} руб.
        Остаток после предоплаты: {cost["remainder"]} руб.
        
        Текущий статус бронирования: {STATUS_RU.get(booking.status, booking.status)}
        
        Открыть бронь в админке:
        {admin_url}
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=settings.OWNER_EMAIL,
        fail_silently=False,
    )
