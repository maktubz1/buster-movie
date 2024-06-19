from django.db import models
from users.models import User


# Create your models here.
class RatingMovies(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default="", blank=True)
    rating = models.CharField(
        max_length=20, choices=RatingMovies.choices, default=RatingMovies.G
    )
    synopsis = models.TextField(null=True, default="", blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="added_by", null=True
    )
