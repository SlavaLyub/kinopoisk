# kinopoisk/views.py
from django.shortcuts import render, get_object_or_404
from .models import Movie, MoviePerson, Genre

def main(request):  # Сами
    # В дальнейшем доделаем
    return render(request, 'kinopoisk/main.html')

def movie_list(request):  # Сами
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/movie_list.html', {
        'movies': movies
    })


def actor_list(request):  # Подсказываем
    actors = MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR)
    return render(request, 'kinopoisk/person_list.html', {
        'persons': actors, 'title': 'Актёры'
    })


def director_list(request):  # Сами
    directors = MoviePerson.objects.filter(role=MoviePerson.RoleType.DIRECTOR)
    return render(request, 'kinopoisk/person_list.html', {
        'persons': directors, 'title': 'Режиссёры'
    })


def genre_list(request):  # Сами
    genres = Genre.objects.all()
    return render(request, 'kinopoisk/genre_list.html', {
        'genres': genres
    })


def movie_detail(request, movie_id):  # Сами
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'kinopoisk/movie_detail.html', {
        'movie': movie
    })

def actor_detail(request, actor_id):  # Напомнить, про раздел Related Name в шпаргалке.
    actor = MoviePerson.objects.get(id=actor_id)
    movies = actor.acted_in_movies.all()
    return render(request, 'kinopoisk/person_detail.html', {
        'person': actor, 'movies': movies
    })


def director_detail(request, director_id):  # Сами
    director = MoviePerson.objects.get(id=director_id)
    movies = director.directed_movies.all()
    return render(request, 'kinopoisk/person_detail.html', {
        'person': director, 'movies': movies
    })


def genre_detail(request, genre_id):  # Сами
    genre = Genre.objects.get(id=genre_id)
    movies = genre.movies.all()
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': genre, 'movies': movies
    })