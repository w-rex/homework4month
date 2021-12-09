from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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


class CinemaValidatedSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=20)

    def validate_name(self, name):
        if Cinema.objects.filter(name=name).count() > 0:
            raise ValidationError("This name is exist")
        return name


class UserCreateSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, min_length=3)
    username = serializers.CharField(max_length=100, min_length=1)

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError("This username exits")
        return username


class UserValidateSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, min_length=3)
    username = serializers.CharField(max_length=100, min_length=1)

