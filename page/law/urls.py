from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком статей
    path('article/', views.article),
    # страница с отзывами
    path('reviews/', views.reviews),
] 