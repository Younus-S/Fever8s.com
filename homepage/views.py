from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Movies

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

# def movies(request):
#   template = loader.get_template('movies.html')
#   return HttpResponse(template.render())

def movies(request):
  mymovies = Movies.objects.all().values()
  template = loader.get_template('movies.html')
  context = {
    'mymovies': mymovies,
  }
  return HttpResponse(template.render(context, request))

# def allmovies(request):
#   mymovies = Movies.objects.all().values()
#   template = loader.get_template('all_movies.html')
#   context = {
#     'mymovies': mymovies,
#   }
#   return HttpResponse(template.render(context, request))

def movie_details(request, id):
  moviedetails = Movies.objects.get(id=id)
  template = loader.get_template('movie_details.html')
  context = {
    'moviedetails': moviedetails,
  }
  return HttpResponse(template.render(context, request))