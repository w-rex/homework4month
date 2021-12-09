

from django.contrib.auth import authenticate
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Movie, Review
from main.serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    return Response(data=data)


@api_view(['GET'])
def genres_review(request):
    movies = Movie.objects.all()
    data = GenresReviewSerializers(movies, many=True).data
    return Response(data=data)


@api_view(['PUT', 'DELETE'])
def cinema_detail_update_delete_view(request, id):
    cinema = Cinema.objects.get(id=id)
    if request.method == 'PUT':
        cinema.name = request.data.get('name', '')
        cinema.save()
        return Response(data={
            'message': 'Tag Updated!',
            'data': CinemaSerializers(cinema).data})
    elif request.method == 'DELETE':
        cinema.delete()
        return Response(data={'message': 'Tag deleted!'})


@api_view(["POST", "GET"])
def cinema_creat_view(request):
    if request.method == "POST":
        name = request.data.get('name')
        serializer = CinemaValidatedSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors})
        cinema = Cinema.objects.create(name=name)
        return Response(data={"message": "Cinema created",
                              "data": CinemaSerializers(cinema).data})

    else:
        cinemas = Cinema.objects.all()
        data = CinemaSerializers(cinemas, many=True).data
        return Response(data=data)



@api_view(["POST"])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                        data={'error': serializer.errors})
    User.objects.create_user(**serializer.validated_data)
    return Response(data={"message": "User created"})



@api_view(["POST"])
def login_create(request):
    serializer = UserValidateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                        data={'errors': serializer.errors})
    user = authenticate(**request.data)
    if user:
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return Response(data={"token": token.key})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


