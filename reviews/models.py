from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Модель Review - представляет собой отзывы glamping
    """

    class Meta:
        ordering = ['-created_at']

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, # При удалении юзера отзыв остается
        null=True, # Разрешает базе данных хранить NULL
        blank=True, # Разрешает оставлять поле пустым в формах
        verbose_name="Автор отзыва",
        related_name="reviews", # ссылка для обратной связи
    )
    author_name = models.CharField(
        verbose_name="Имя автора (для seed/гостей)",
        max_length=120,
        blank=True,
        null=True,
    )

    author_avatar = models.ImageField(
        upload_to="reviews/avatars/", # куда сохраняем аватары отзывов,
        blank = True,
        null=True,
        verbose_name="Аватары (для seed/гостей)",
    )

    text = models.TextField(
        verbose_name="Текст отзыва",
        validators=[
            MaxLengthValidator(3000, message="Отзыв слишком длинный (максимум 3000 символов)"),
        ]
    )
    rating = models.PositiveIntegerField(
        verbose_name="Рейтинг-оценка, от 1 до 5",
        validators=[
            MinValueValidator(1, message="Оценка не может быть ниже 1"),
            MaxValueValidator(5, message="Оценка не может быть выше 5"),
        ],
        help_text="Поставьте оценку от 1 до 5 звезд"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания отзыва!"
    )


    def __str__(self):
        # Защита от удаленного пользователя
        author = self.user.username if self.user else "Удаленный пользователь"
        # Обрезаем длинный текст, чтобы не ломать админку
        short_text = (
            self.text[:30] + "..." if len(self.text) > 30 else self.text
        )
        return f"Отзыв от {author}: «{short_text}»"


    def stars(self):
        return "★" * self.rating + "☆" * (5 - self.rating)



class ReviewImage(models.Model):
    """
    Модель для изображений отзывов
    """
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Отзыв",
    )
    image = models.ImageField(
        upload_to="reviews/images/"
    )

    def __str__(self):
        return f"Image for review {self.review_id}"