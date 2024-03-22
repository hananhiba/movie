from django.shortcuts import render
from MovieApp.models import Movie
from django.db.models import Q


# Create your views here.


def SearchResults(request):
    movie = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movie = Movie.objects.all().filter(Q(name__icontains=query) | Q(description__contains=query))
    return render(request, "search.html", {'query': query, 'movie': movie})
