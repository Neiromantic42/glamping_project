from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


@login_required
def profile(request):
    """
    Страница профиля пользователя
    """
    profile = request.user.profile

    if request.method == 'POST':
        # Получаем данные из формы
        display_name = request.POST.get('display_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        avatar = request.FILES.get('avatar')

        # Обновляем данные
        if email:
            request.user.email = email
            request.user.save()

        profile.display_name = display_name
        profile.phone = phone if phone else None

        if avatar:
            profile.avatar = avatar

        profile.save()

        messages.success(request, 'Профиль успешно обновлен!')
        return redirect('accounts:profile')

    context = {
        'user': request.user,
        'profile': profile,
    }

    return render(request, 'users/profile.html', context)