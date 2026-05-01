from django.urls import path
from .views import payment

app_name = 'payment'

urlpatterns = [
    path('<int:booking_id>/', payment, name='payment_page')
]