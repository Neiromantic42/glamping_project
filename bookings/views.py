import logging
from .models import Booking
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from bookings.forms import BookingForm

logger = logging.getLogger(__name__)


def booking(request: HttpRequest) -> HttpResponse:
    """
    Страница бронирования
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            logger.info("Форма валидна")
            print(form.cleaned_data)
            return redirect('glamping:home_page')
        else:
            print(form.errors)
            logger.warning(form.errors)
            return render(request, "bookings/booking.html", {"form": form})

    elif request.method == "GET":
        form = BookingForm()
        return render(request, 'bookings/booking.html', {"form": form})


def get_dates(request: HttpRequest) -> JsonResponse:
    """
    Метод вернет занятые даты перед инициализацией календаря

    В booking.html
    """
    bookings = Booking.objects.filter(status="confirmed") # получаем все подтвержденные брони
    data = [
        {
            "from": i.check_in_date.isoformat(),
            "to": i.check_out_date.isoformat()
        }
        for i in bookings
    ]
    return JsonResponse(data=data, safe=False)
