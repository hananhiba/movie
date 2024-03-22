from django.db import models
from django.urls import reverse
from credentials.views import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('MovieApp:MoviesByCategory', args=[str(self.id)])

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    actors = models.CharField(max_length=200)
    release_date = models.DateField()
    image = models.ImageField(upload_to='movie')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.URLField()
    added_by=models.ForeignKey(User,on_delete=models.CASCADE,default='2')

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def get_url(self):
        return reverse('MovieApp:detail', args=[str(self.category.id), str(self.id)])

    def __str__(self):
        return self.name
