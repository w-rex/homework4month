from rest_framework import serializers

from main.models import *


class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class Genres(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'



