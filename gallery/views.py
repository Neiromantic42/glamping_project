from django.shortcuts import render
from .models import GalleryImage


def gallery(request):
    """
    Страница галереи глемпинга
    """
    images = GalleryImage.objects.filter(is_active=True)

    context = {
        'images': images,
    }

    return render(request, 'gallery/gallery.html', context)