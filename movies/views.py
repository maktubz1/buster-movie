from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404


from .permission import IsEmployeeOrRedOnly
from rest_framework.pagination import PageNumberPagination


class MovieDetailView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrRedOnly]

    def get(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    def delete(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrRedOnly]

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        result = self.paginate_queryset(movies, req)
        serializer = MovieSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
