from django.contrib.auth.models import User
from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    cinema = models.ForeignKey(Cinema, null=True, blank=True, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    reviews = models.ForeignKey(Movie, null=True, related_name='reviews',  blank=True, on_delete=models.CASCADE)