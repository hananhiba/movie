from django.contrib import admin
from .models import Category, Movie


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name', ]}


admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'description', 'category', 'actors', 'link']
    prepopulated_fields = {'slug': ['name', ]}
    list_editable = ['image', 'category']


admin.site.register(Movie, MovieAdmin)
