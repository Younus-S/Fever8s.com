from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('members/', views.members, name='homepage'),
]