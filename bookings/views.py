import logging
from .models import Booking
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from bookings.forms import BookingForm
from bookings.services.booking_service import is_dates_available, create_booking
from glamping.models import Glamping

logger = logging.getLogger(__name__)


def booking(request: HttpRequest) -> HttpResponse:
    """
    Страница бронирования
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            logger.info("Форма валидна")
            print(form.cleaned_data)
            glamping = get_object_or_404(Glamping, id=1)
            is_available = is_dates_available(
                glamping=glamping,
                check_in=form.cleaned_data["check_in_date"],
                check_out=form.cleaned_data["check_out_date"]
            )
            # если пересечений дат нет, создаем запись бронирования
            if is_available:
                booking = create_booking(form=form, glamping=glamping)
                return redirect('payment:payment_page', booking_id=booking.pk)
            form.add_error(None, "Эти даты уже заняты")
            return render(request, "bookings/booking.html", {"form": form})

        else:
            print(form.errors)
            logger.warning(form.errors)
            return render(request, "bookings/booking.html", {"form": form})

    elif request.method == "GET":
        form = BookingForm()
        glamping = get_object_or_404(Glamping, id=1)
        additional_price = glamping.extra_guest_price
        single_night_extra_guest_price = glamping.single_night_extra_guest_price

        return render(request, 'bookings/booking.html',
                      {
                          "form": form,
                          "extra_guest_price": additional_price,
                          "single_night_extra_guest_price": single_night_extra_guest_price,
                      }
                      )


def get_dates(request: HttpRequest) -> JsonResponse:
    """
    Метод вернет занятые даты перед инициализацией календаря

    В booking.html
    """
    bookings = Booking.objects.filter(status="confirmed")  # получаем все подтвержденные брони
    data = [
        {
            "from": i.check_in_date.isoformat(),
            "to": i.check_out_date.isoformat()
        }
        for i in bookings
    ]
    return JsonResponse(data=data, safe=False)
