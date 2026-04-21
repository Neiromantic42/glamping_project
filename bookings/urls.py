from django.urls import path
from .views import booking

app_name = 'bookings'

urlpatterns = [
    path('', booking, name='booking')
]