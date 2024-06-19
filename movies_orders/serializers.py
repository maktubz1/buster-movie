from rest_framework import serializers
from .models import MovieOrder
from users.models import User
from movies.models import Movie


class MovieOrderSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField(read_only=True, source="movie.title")
    purchased_by = serializers.SerializerMethodField(
        read_only=True, source="user.email"
    )

    class Meta:
        model = MovieOrder
        fields = ["id", "title", "purchased_by", "purchased_at", "price"]

    def get_title(self, obj):
        return obj.movie.title

    def get_purchased_by(self, obj):
        return obj.user.email

    def create(self, validated_data):
        # user = self.context["request"].user
        # movie_id = self.context["view"].kwargs.get("movie_id")
        # movie = Movie.objects.get(id=movie_id)
        return MovieOrder.objects.create(**validated_data)
