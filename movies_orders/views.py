from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from movies_orders.serializers import MovieOrderSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class MovieOrderView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movie_id: int) -> Response:
        movie_data = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=req.user, movie=movie_data)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result = self.paginate_queryset(movies, request, view=self)

        serializer = MovieOrderSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)
