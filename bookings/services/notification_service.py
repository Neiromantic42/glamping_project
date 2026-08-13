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


def notify_the_guest_about_the_booking(booking, cost):
    """
    Функция для отправки эмейла гостю глэмпинга
    """
    subject = "/\ КАМА ГЛ Подтверждение бронирования"

    message = f"""
        /\ КАМА ГЛ

        Спасибо за выбор КАМА ГЛ!

        Вы только что забронировали место, где можно ненадолго забыть
        о городе, выдохнуть и провести время на природе у Камы.

        Мы рады принять Вас и уже подготовили всё необходимое для
        Вашего комфортного отдыха.

        Ниже — подробности Вашего бронирования и расчёт стоимости.
        Сохраните это письмо — здесь собрана вся информация по Вашей заявке.

            
        Бронирование №{booking.id}
        Статус: Ожидает оплаты / подтверждения
        
        Данные гостя
        Имя: {booking.name}
        Телефон: {booking.phone}
        Email: {booking.email}
        
        Период проживания
        Заезд: {booking.check_in_date}
        Выезд: {booking.check_out_date}
        Количество ночей: {cost["nights"]}
        
        Гости
        Всего гостей: {booking.guests_count}
        Кол-во дополнительно оплачиваемых гостей: {cost["extra_guests_count"]}
        Стоимость дополнительно оплачиваемых гостей: {cost["guest_fee"]} руб.
        
        Стоимость
        Общая стоимость: {cost["total_price"]}
        Предоплата: {cost["prepayment"]} руб.
        Остаток после предоплаты: {cost["remainder"]} руб.
        
        
        Если у Вас появятся вопросы, мы всегда на связи:

        WhatsApp:
        https://wa.me/79178521635?text=Здравствуйте!%20У%20меня%20есть%20вопрос%20по%20бронированию
    
        Наш сайт:
        https://kama-glamping.ru/
        
        
        С нетерпением ждём Вас и желаем отличного отдыха!
        Команда /\ КАМА ГЛ
    """

    send_mail(
        subject=subject,  # Тема письма, которую увидит гость в почтовом ящике
        message=message,  # Основной текст письма с данными бронирования и расчётом
        from_email=settings.DEFAULT_FROM_EMAIL,  # Email-адрес отправителя из настроек Django
        recipient_list=[booking.email],  # Email гостя, указанный при бронировании
        fail_silently=False,  # Если отправка не удалась — выбрасываем ошибку
    )