from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from MovieApp.forms import MovieForm
from MovieApp.models import Movie, Category


# Create your views here.

def index(request, c_slug=None):
    if c_slug != None:
        category = Category.objects.get(slug=c_slug)
        movie = Movie.objects.filter(category=category)
    else:
        movie = Movie.objects.all()
        category = Category.objects.all()
    return render(request, "index.html", {'movie': movie,'category':category})


def detail(request, movie_id):
    movie1 = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie1})


def AllMovies(request, c_slug=None):
    if c_slug != None:
        category = Category.objects.get(slug=c_slug)
        my_movies = Movie.objects.all().filter(category=category)
    else:
        my_movies = Movie.objects.all()
    return render(request, "AllMovies.html", {"movie": my_movies})


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        release_date = request.POST['release_date']
        description = request.POST['description']
        movie_cat = request.POST['category']
        category = Category.objects.get(id=movie_cat)
        image = request.FILES['image']
        actors = request.POST['actors']
        slug = slugify(name)
        link = request.POST['link']
        if not request.user.is_authenticated:
            messages.info(request, "Not Registered as User")
            return redirect('credentials:signup')
        else:
            user = User.objects.get(id=request.user.id)
            movie = Movie(name=name, release_date=release_date, link=link, actors=actors, description=description,
                          image=image, category=category, slug=slug, added_by=user)
            movie.save()
            return redirect("/")
    return render(request, "add.html")


def update(request, id):
    form=None
    movie = Movie.objects.get(id=id)
    if movie.added_by == request.user:
        form = MovieForm(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        messages.info(request,
                      "You are not authorised to update this movie. Only added user have permitted to update. ")
    return render(request, "update.html", {'form': form, 'movie': movie})


def delete(request, id):
    movie = Movie.objects.get(id=id)
    if request.user == movie.added_by:
        if request.method == 'POST':
            movie.delete()
            return redirect('/')
    else:
        messages.info(request, "You are not permitted to delete this movie. Only added user can delete a movie")
    return render(request, "delete.html")


def category(request):
    cat = Category.objects.all()
    movie=Movie.objects.all()
    return render(request, "category.html", {'cat': cat,'movie':movie})


def about(request):
    return render(request, "aboutUs.html")
