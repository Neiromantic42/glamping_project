from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('', views.cinema, name='cinema'),
    path('book-session/', views.book_session, name='book_session'),
]