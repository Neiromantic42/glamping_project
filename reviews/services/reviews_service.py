from datetime import date
from bookings.models import Booking
from reviews.models import Review


def get_review_permission(user):
    if not user.is_authenticated:
        return "not_auth"

    email = user.email
    if not email:
        return "no_booking"

    review_exists = Review.objects.filter(user=user).exists()
    if review_exists:
        return "already_reviewed"

    booking = (
        Booking.objects
        .filter(email=email, status="confirmed")
        .order_by("-check_out_date")
        .first()
    )

    if not booking:
        return "no_booking"

    delta = (date.today() - booking.check_out_date).days

    if delta < 0:
        return "no_booking"

    if delta > 14:
        return "expired"

    return "can_review"