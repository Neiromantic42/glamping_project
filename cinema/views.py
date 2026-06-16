from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import CinemaBooking
from .services.movie_show_notification import (
    cinema_showtime_notification,
    send_an_email_confirming_your_movie_theater_booking
)
from django.conf import settings


def cinema(request):
    """
    Страница кинотеатра с описанием и формой заказа
    """

    # Получаем настройку, включена ли платная услуга (можно добавить в settings.py)
    cinema_booking_enabled = getattr(settings, 'CINEMA_BOOKING_ENABLED', True)

    context = {
        'cinema_booking_enabled': cinema_booking_enabled,
    }

    return render(request, 'cinema/cinema.html', context)


@require_http_methods(["POST"])
def book_session(request):
    """
    Обработка заказа премиум сеанса
    """

    try:
        # Получаем данные из формы
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        movie_name = request.POST.get('movie_name', '').strip()
        session_date = request.POST.get('session_date', '').strip()
        session_time = request.POST.get('session_time', '').strip()
        comments = request.POST.get('comments', '').strip()

        # Базовая валидация
        if not all([name, phone, movie_name, session_date, session_time, comments]):
            messages.error(request, 'Пожалуйста, заполните все обязательные поля')
            return redirect('cinema:cinema')

        # Создаем заказ в базе данных
        booking = CinemaBooking.objects.create(
            name=name,
            phone=phone,
            email=email if email else None,
            movie_name=movie_name,
            session_date=session_date,
            session_time=session_time,
            comments=comments,
            status='pending'
        )
        # здесь вызываем функцию отправки письма хосту и затем клиенту
        cinema_showtime_notification(booking=booking)
        send_an_email_confirming_your_movie_theater_booking(booking=booking)

        # Отправляем успешное сообщение
        messages.success(
            request,
            f'✅ Спасибо, {name}! Ваш заказ на фильм "{movie_name}" принят. '
            f'Мы свяжемся с вами по номеру {phone} в течение 2 часов для подтверждения.'
        )

        return redirect('glamping:home_page')

    except Exception as e:
        messages.error(request, f'❌ Ошибка при создании заказа: {str(e)}')
        return redirect('cinema:cinema')