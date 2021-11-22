from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Movie, Review
from main.serializers import *


@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializers(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_item(request, id):
    movie = Movie.objects.get(id=id)
    data = MovieSerializers(movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review(request):
    movies = Movie.objects.all()
    data = ReviewFilmSerializers(movies, many=True).data
    return Response(data=data)\


@api_view(['GET'])
def genres_review(request):
    movies = Movie.objects.all()
    data = GenresReviewSerializers(movies, many=True).data
    return Response(data=data)




