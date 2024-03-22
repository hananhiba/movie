from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from MovieApp.models import Movie
from Review.models import Review


# Create your views here.


def add_review(request, slug):
    mov = Movie.objects.get(slug=slug)
    if request.user.is_authenticated:
        if request.method == 'POST':
            review = request.POST['review']
            rating = request.POST['rating']
            date = request.POST['date']
            user = User.objects.get(id=request.user.id)
            add = Review(user=user, review=review, date=date, rating=rating, movie=mov)
            add.save()
            return redirect('Review:add_reviews',slug)
    else:
        messages.info(request,"Login to add reviews")
        return redirect('credentials:login')
    return render(request, "review.html", {'mov': mov})







