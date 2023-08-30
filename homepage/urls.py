from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('movies/', views.movies, name='movies'),
    path('Games/', views.games, name='games'),
    path('Books/', views.books, name='games'),
    path('Songs/', views.songs, name='games'),
    path('Comics/', views.comics, name='games'),
    path('Videos/', views.videos, name='games'),
    path('Software/', views.software, name='games'),
    path('TVShows/', views.tvshows, name='games'),
    path('movies/movie_details/<int:id>', views.movie_details, name='details'),
    path('movie_details/', views.movie_details, name='details'),
]