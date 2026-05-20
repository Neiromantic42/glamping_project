from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from users.forms import CustomUserCreationForm
import logging



logger = logging.getLogger(__name__)



def register(request):
    """
    Страница регистрации
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirm = request.POST.get('password2')

        # TODO: Логика регистрации
        # Проверка паролей, создание пользователя, отправка email
        form = CustomUserCreationForm(request.POST) # Создаем дефолтную форму и передаем данные запроса
        logger.info(f"Ошибка формы: {form.errors}")
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('glamping:home_page')
        else:
            messages.error(request, 'Исправьте ошибки в форме')
            return render(request, 'users/register.html', {'form': form})

    return render(request, 'users/register.html')


def login(request):
    """
    Страница входа
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        # TODO: Логика аутентификации
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            if not remember_me:
                request.session.set_expiry(0)  # Сессия закрывается при закрытии браузера
            return redirect('reviews:reviews')
        else:
            messages.error(request, 'Неверный логин или пароль')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')


def logout_view(request):
    """
    Функция для выхода пользователя из сессии
    """
    if request.method == 'POST':
        logout(request=request)
    return redirect('glamping:home_page')



def password_reset(request):
    """
    Страница восстановления пароля (заглушка)
    """
    # TODO: Создать страницу восстановления пароля
    messages.info(request, 'Восстановление пароля временно недоступно. Свяжитесь с администратором.')
    return redirect('users:login')