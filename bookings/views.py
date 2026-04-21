from django.contrib import messages
from django.shortcuts import render, redirect


def booking(request):
    """
    Страница бронирования
    """
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = request.POST.get('guests')

        # TODO: Здесь будет логика сохранения в БД
        # Пока просто выводим сообщение
        messages.success(request, f'Спасибо, {name}! Ваша бронь получена. Мы свяжемся с вами по телефону {phone}.')

        return redirect('glamping:home_page')

    return render(request, 'bookings/booking.html')