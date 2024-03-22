from django import forms
from .models import Movie, Category


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'image', 'category', 'release_date', 'actors', 'link']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
