from django.core.mail import send_mail
from django.conf import settings


def cinema_showtime_notification(booking):
    """
    Функция уведомляет хоста глемпинга о брони сеанса кинотеатра
    """
    admin_url = f"https://kama-glamping.ru/admin/cinema/cinemabooking/{booking.id}/change/"

    subject = "Пользователь перешел к бронированию сеанса кинотеатра"

    message = f"""
    Пользователь перешел к подтверждению бронирования сеанса кинотеатра:
    
    Имя клиента: {booking.name}
    Телефон: {booking.phone}
    Почта: {booking.email}
    
    Название выбранного фильма: {booking.movie_name}
    Дата сеанса: {booking.session_date}
    Время начала сеанса: {booking.session_time}
    Коментарий клиента: {booking.comments}
    
    Служебная информация:
    Дата создания заказа: {booking.created_at}
    
    Админка: {admin_url}
    
    Внимание, утони статус оплаты!
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=settings.OWNER_EMAIL,
        fail_silently=False,
    )


def send_an_email_confirming_your_movie_theater_booking(booking):
    """
    Уведомление по Email клиента глемпинга об удачной брони!
    """
    subject = "Спасибо за бронирование сеанса кинотеатра в  /\ Кама ГЛ"

    message = f"""
    Здравствуйте, {booking.name}!
    
    Спасибо за бронирование нашего Кинотеатра в /\ Кама ГЛ и своевременное внесение оплаты!
    
    Детали бронирования сеанса: 
    Выбранный Вами фильм: {booking.movie_name}
    Дата сеанса: {booking.session_date}
    Время начала показа: {booking.session_time}
    
    Желаем хорошего просмотра!
    """

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[booking.email],
        fail_silently=False,
    )