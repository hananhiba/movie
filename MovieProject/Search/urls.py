from django.urls import path
from . import views
app_name='Search'

urlpatterns = [
    path('search',views.SearchResults,name='SearchResults'),

]
