from rest_framework import serializers

from main.models import *


class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class GenresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    cinema = CinemaSerializers()
    genres = GenresSerializers(many=True)
    reviews = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        fields = 'title description cinema genres reviews'.split()


class ReviewFilmSerializers(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        fields = 'reviews'.split()


class GenresReviewSerializers(serializers.ModelSerializer):
    genres = GenresSerializers(many=True)

    class Meta:
        model = Movie
        fields = 'genres'.split()





