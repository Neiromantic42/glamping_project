from django.shortcuts import render

def about(request):
    """
    Страница "О нас"
    """
    return render(request, 'info/about.html')
