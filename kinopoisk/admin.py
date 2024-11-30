from django.contrib import admin
from .models import MoviePerson, Genre, Movie, MovieReview

admin.site.register(MoviePerson)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieReview)