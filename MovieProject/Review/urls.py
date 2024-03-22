from django.urls import path
from . import views
app_name='Review'

urlpatterns = [
    path('review/<slug:slug>/',views.add_review,name='add_reviews'),

]
