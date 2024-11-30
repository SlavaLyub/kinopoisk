# kinopoisk/urls.
from django.urls import path
from .views import *

app_name = 'kinopoisk'
urlpatterns = [
    path('', main, name='main'),  # Главная страница.

    path('movies/', movie_list, name='movie_list'),  # Список всех фильмов.
    path('actors/', actor_list, name='actor_list'),  # Список всех актеров.
    path('directors/', director_list, name='director_list'),  # Список всех режиссеров.
    path('genres/', genre_list, name='genre_list'),  # Список всех жанров.

    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),  # Детали фильма.
    path('actor/<int:actor_id>/', actor_detail, name='actor_detail'),  # Детали актера + его фильмы.
    path('director/<int:director_id>/', director_detail, name='director_detail'),  # Детали режиссера + его фильмы.
    path('genre/<int:genre_id>/', genre_detail, name='genre_detail'),  # Фильмы по жанру.
]
