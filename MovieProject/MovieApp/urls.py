from django.urls import path
from . import views

app_name = 'MovieApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('all-movies/',views.AllMovies,name='AllMovies'),
    path('movie_cat/<slug:c_slug>',views.AllMovies,name='MoviesByCategory'),
    path('add/', views.add, name='add'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('category/',views.category,name='category'),
    path('about/',views.about,name='about'),




]
