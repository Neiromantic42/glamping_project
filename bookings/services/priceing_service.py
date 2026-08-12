from decimal import Decimal


def calculate_the_booking_cost(booking, glamping):
    """
    Функция расчета стоимости бронирования

    Получает на вход обьекты глемпинга и букинга
    """
    # Получаем кол-во ночей
    nights = (booking.check_out_date - booking.check_in_date).days
    # вычисляем тариф
    if nights == 1:
        price_per_night = glamping.single_night_price
        extra_guest_price = glamping.single_night_extra_guest_price
        actual_extra_guest_price = glamping.single_night_extra_guest_price
    else:
        price_per_night = glamping.price_per_night
        extra_guest_price = glamping.extra_guest_price
        actual_extra_guest_price = glamping.extra_guest_price

    # доп гости
    extra_guests_count = max(0, booking.guests_count - 2)
    # доплата за гостей (ВАЖНО: умножаем на nights)
    guest_fee = extra_guests_count * extra_guest_price * nights
    # итог
    total_price = (nights * price_per_night) + guest_fee
    prepayment = total_price * Decimal("0.5")
    price_data = {
        "nights": nights,  # количество ночей
        "price_per_night": price_per_night,  # цена за ночь
        "extra_guest_price": extra_guest_price,  # цена за одного доп. гостя за ночь
        "extra_guests_count": extra_guests_count,  # количество доп. гостей
        "guest_fee": guest_fee,  # общая доплата за всех доп. гостей
        "total_price": total_price,  # общая стоимость бронирования
        "prepayment": prepayment,  # сумма предоплаты 50%
        "remainder": total_price - prepayment,  # остаток после предоплаты
    }
    return price_data