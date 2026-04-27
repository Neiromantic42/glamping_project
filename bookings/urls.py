from django.urls import path
from .views import booking, get_dates

app_name = 'bookings'

urlpatterns = [
    path('', booking, name='booking'), # главная страница бронирования
    path("api/bookings/dates/", get_dates, name="booking-dates")
]