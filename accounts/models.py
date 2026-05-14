from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    """
    Модель профиля, расширяющая данные стандартного пользователя
    """
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    phone = PhoneNumberField(
        null=True, blank=True, unique=True, region="RU",
        verbose_name="Телефон пользователя"
    )
    # Отображаемое имя в профиле
    display_name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Отображаемое в профиле имя"
    )
    # Дата создания профиля
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Профиль пользователя: {self.user.username}"
