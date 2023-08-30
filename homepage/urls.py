from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('movies/', views.movies, name='movies'),
    path('movies/movie_details/<int:id>', views.movie_details, name='details'),
    path('movie_details/', views.movie_details, name='details'),
]