from datetime import date

from django import forms # Импортируем модуль forms из Django для работы с формами
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.validators import RegexValidator

from bookings.models import Booking



class BookingForm(forms.ModelForm):
    """
    Форма для валидации данных бронирования глемпинга

    введенных в поля на станице
    """
    class Meta: # внутренний класс с настройками формы
        model = Booking # указываем, с какой моделью связана форма
        # перечисляем поля, которые будут в форме
        fields = "name", "phone", "email", "check_in_date", "check_out_date", "guests_count"

    def clean_name(self):
        """
        валидируем имя клиента
        """
        name = self.cleaned_data.get("name")

        if not name:
            raise forms.ValidationError("Имя обязательно")
        if len(name) < 2:
            raise forms.ValidationError("Имя слишком короткое")
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Имя не должно содержать цифр")
        return name

    # def clean_guests_count(self):
    #     """
    #     Валидируем кол-во гостей
    #     """
    #     guests_count = self.cleaned_data.get("guests_count")
    #     guests_count = int(guests_count)
    #     return guests_count


    def clean(self):
        """
        Валидируем даты
        """
        cleaned_data = super().clean()

        check_in_date = cleaned_data.get("check_in_date")
        check_out_date = cleaned_data.get("check_out_date")

        if not check_in_date or not check_out_date:
            raise forms.ValidationError("Даты - выезда, заезда обязательны!")
        if check_in_date >=check_out_date:
            raise forms.ValidationError("Дата заезда не может быть позже или равна дте выезда")
        if check_in_date < date.today():
            raise forms.ValidationError("Дата заезда не может быть в прошлом")
        if (check_out_date - check_in_date).days > 30:
            raise forms.ValidationError("Максимальный срок бронирования — 30 дней")
