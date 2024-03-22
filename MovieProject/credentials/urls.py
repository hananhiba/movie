from django.urls import path
from . import views

app_name = 'credentials'

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/<int:user_id>/', views.userview, name='user-view'),

]
