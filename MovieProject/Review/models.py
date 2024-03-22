from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from MovieApp.models import Movie


# Create your models here.

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def get_url(self):
        return reverse('MovieApp:detail', args=[str(self.movie.id), str(self.id)])

    def __str__(self):
        return f"{self.movie.name}:{self.rating}"

