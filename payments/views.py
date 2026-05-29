from decimal import Decimal
from payments.services.payment_notice import (
    notify_owner_payment_attempt,
    send_booking_confirmation_email
)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from bookings.models import Booking
from glamping.models import Glamping
import logging

logger = logging.getLogger(__name__)


def payment(request, booking_id: int):
    """
    Страница оплаты бронирования
    """
    # TODO: Получить booking из БД
    booking = get_object_or_404(Booking, id=booking_id)
    glamping = get_object_or_404(Glamping, id=1)
    nights = (booking.check_out_date - booking.check_in_date).days
    extra_guests_count = (booking.guests_count - 2)
    guest_fee = extra_guests_count * glamping.extra_guest_price

    if booking.guests_count <=2:
        total_price = nights * glamping.price_per_night
        prepayment = total_price * Decimal(0.5)
    else:
        total_price = (nights * glamping.price_per_night) + ((booking.guests_count - 2) * glamping.extra_guest_price)
        prepayment = total_price * Decimal(0.5)

    if request.method == 'POST':
        # Пользователь нажал "Я оплатил"
        # TODO: Изменить статус на PENDING_PAYMENT
        messages.success(request, 'Спасибо! Мы проверяем платеж.')
        try:
            notify_owner_payment_attempt(
                booking,
                nights,
                total_price,
                prepayment,
                extra_guests_count,
                guest_fee,
            )
            send_booking_confirmation_email(
                booking,
                nights,
                total_price,
                prepayment,
                extra_guests_count,
                guest_fee,
            )
        except Exception as e:
            logger.info(f"Ошибка отправки письма: {e}")

        return redirect('glamping:home_page')

    context = {
        'booking': {
            'name': booking.name,
            'phone': booking.phone,
            'email': booking.email,
            'check_in': booking.check_in_date,
            'check_out': booking.check_out_date,
            'guests_count': booking.guests_count,
            'extra_guests_count': extra_guests_count,
            'extra_guest_price': glamping.extra_guest_price,
            'guest_fee': guest_fee,
            'nights': nights,
            'total_price': total_price,
            'prepayment': prepayment,
            'remainder': total_price - prepayment, # остаток к оплате после предоплаты
        },
        'payment_details': {
            'phone': glamping.phone,
            'bank': 'МТС Деньги',
            'recipient': 'Алексей С.',
        }
    }

    return render(request, 'payments/payment.html', context)