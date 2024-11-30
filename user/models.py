from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # add to sett AUTH_USER
    favorite_movies = models.ManyToManyField(
        'kinopoisk.Movie',
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
