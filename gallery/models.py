from django.db import models


class GalleryImage(models.Model):
    """
    Изображения для галереи глемпинга
    """
    ORIENTATION_CHOICES = [
        ('horizontal', 'Горизонтальная'),
        ('vertical', 'Вертикальная'),
        ('square', 'Квадратная'),
    ]

    image = models.ImageField(
        upload_to='gallery/',
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    orientation = models.CharField(
        max_length=20,
        choices=ORIENTATION_CHOICES,
        default='horizontal',
        verbose_name='Ориентация'
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Порядок сортировки'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активно'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Фотография галереи'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.title or f'Фото #{self.id}'