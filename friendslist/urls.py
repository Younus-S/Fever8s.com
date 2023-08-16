from django.urls import path
from . import views

urlpatterns = [
    path('friendslist/', views.friends, name='friends'),
    path('friendslist/f1', views.friend1, name='friends'),
    path('friendslist/f2', views.friend2, name='friends'),
    path('friendslist/f3', views.friend3, name='friends'),
    path('friendslist/f4', views.friend4, name='friends'),
    path('friendslist/f5', views.friend5, name='friends'),
    path('friendslist/f6', views.friend6, name='friends'),
    path('friendslist/f7', views.friend7, name='friends'),
    path('friendslist/f8', views.friend8, name='friends'),
    path('friendslist/f9', views.friend9, name='friends'),
    path('friendslist/f10', views.friend10, name='friends'),
    
]