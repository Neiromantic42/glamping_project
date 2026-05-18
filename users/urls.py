from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'), # регистрация
    path('login/', views.login, name='login'), # аутентификация
    path('logout/', views.logout_view, name='logout'), # выход из сессии
    path('password-reset/', views.password_reset, name='password_reset'), # забыл пароль путь
]