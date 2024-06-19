from django.db import models
from users.models import User
from movies.models import Movie


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_movie")

    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="order_movie"
    )
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Movie Order - id: {self.id}, price: {self.price}, purchased at: {self.purchased_at}"
