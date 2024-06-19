from rest_framework import serializers
from movies.models import RatingMovies, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    synopsis = serializers.CharField(default="")
    rating = serializers.ChoiceField(
        choices=RatingMovies.choices, default=RatingMovies.G
    )
    duration = serializers.CharField(max_length=10, default="")
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data) -> Movie:
        return Movie.objects.create(**validated_data)
