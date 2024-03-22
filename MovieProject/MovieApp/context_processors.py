from MovieApp.models import Category


def MovieCategories(request):
    categories = Category.objects.all()
    return dict(movie_cat=categories)


