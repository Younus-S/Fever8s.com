from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Movies(models.Model):
  moviename = models.CharField(max_length=255)
  category = models.CharField(max_length=255)
  details = models.CharField(max_length=255)
  
  def __str__(self):
    return f"{self.moviename}"