from django.urls import path
from .views import home

app_name = 'glamping'

urlpatterns = [
    path('', home, name='home_page'),# Главная страница
]