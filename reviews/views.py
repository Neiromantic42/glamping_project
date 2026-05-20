from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review, ReviewImage
from reviews.services.reviews_service import get_review_permission
import logging

logger = logging.getLogger(__name__)


def reviews(request):
    """
    Страница отзывов
    """
    reviews_list = Review.objects.select_related('user__profile').prefetch_related('images').all()

    logger.info("Загружена страница отзывов. Кол-во отзывов: %s", reviews_list.count())
    permission = get_review_permission(user=request.user)
    return render(request, 'reviews/reviews.html', {
        'reviews': reviews_list,
        "permission": permission
    })


@login_required
def add_review(request):
    """
    Добавление отзыва
    """
    logger.info("=== ADD REVIEW START ===")
    logger.info("Method: %s", request.method)
    logger.info("User: %s", request.user)

    if request.method == 'POST':

        logger.info("POST DATA: %s", request.POST)
        logger.info("FILES: %s", request.FILES)

        text = request.POST.get('text')
        rating = request.POST.get('rating')

        logger.info("Parsed text: %s", text)
        logger.info("Parsed rating: %s", rating)

        if not text or not rating:
            logger.warning("Empty text or rating")
            messages.error(request, "Заполни текст и рейтинг")
            return redirect('reviews:reviews')


        # email = getattr(request.user, "email", None)
        # logger.info(f"Email for user: {email}")
        # if not can_user_review_booking(email=email):
        #     messages.error(request, "Вы можете оставить отзыв только в течение 14 дней после проживания")
        #     return redirect('reviews:reviews')

        try:
            review = Review.objects.create(
                user=request.user,
                text=text,
                rating=int(rating),
            )

            logger.info("Review created with ID: %s", review.id)

        except Exception as e:
            logger.exception("ERROR while creating review")
            messages.error(request, "Ошибка при создании отзыва")
            return redirect('reviews:reviews')

        images = request.FILES.getlist('images')
        logger.info("Images count: %s", len(images))

        for img in images:
            try:
                ReviewImage.objects.create(
                    review=review,
                    image=img
                )
                logger.info("Image saved for review %s", review.id)
            except Exception:
                logger.exception("ERROR saving image")

        messages.success(request, 'Спасибо за ваш отзыв!')
        logger.info("=== ADD REVIEW SUCCESS ===")

        return redirect('reviews:reviews')

    logger.warning("Non-POST request to add_review")
    return redirect('reviews:reviews')