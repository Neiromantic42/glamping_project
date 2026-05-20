from django.shortcuts import render, get_object_or_404
from .models import Glamping
from django.db.models import Avg, Count
from reviews.models import Review
import logging


logger = logging.getLogger(__name__)

def home(request):
    """
    Главная страница Глемпинга
    """
    glamping = get_object_or_404(Glamping, id=1)

    logger.info(f'Текущий глемпинг: {glamping}')

    reviews_satats = Review.objects.aggregate(
        avg_rating=Avg('rating'),
        total_reviews=Count('id')
    )

    context = {
        'glamping': glamping,
        "avg_rating": round(reviews_satats['avg_rating'] or 0, 1),
        "reviews_count": reviews_satats["total_reviews"],
    }

    return render(request, 'glamping/home.html', context)