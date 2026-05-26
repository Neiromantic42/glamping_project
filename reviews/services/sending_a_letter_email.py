from django.core.mail import send_mail
from django.conf import settings


def get_a_letter_send(review):
    """
    Уведомление владельца о новом отзыве
    """
    reviews_url = "https://kama-glamping.ru/reviews/"
    subject = "/\ Кама ГЛ Пользователь оставил отзыв /\ Кама ГЛ !"

    user_name = (
        review.user.username if review.user else review.author_name
    )

    message = f"""
    /\ Кама ГЛ Новый отзыв! /\ Кама ГЛ
    
    Автор: {user_name}
    Email: {review.user.email if review.user else "__"}
    Рейтинг: {review.rating}
    
    Текст:\n
    {review.text}
    
    Открыть комментарии на /\ Кама ГЛ: {reviews_url}
    """


    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=settings.OWNER_EMAIL,
        fail_silently=False
    )