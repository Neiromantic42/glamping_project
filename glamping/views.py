from django.shortcuts import render, get_object_or_404
from .models import Glamping
import logging


logger = logging.getLogger(__name__)

def home(request):
    """
    Главная страница Глемпинга
    """
    glamping = get_object_or_404(Glamping, id=1)

    logger.info(f'Текущий глемпинг: {glamping}')

    context = {
        'glamping': glamping
    }

    return render(request, 'glamping/home.html', context)