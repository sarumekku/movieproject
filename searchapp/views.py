

# Create your views here.
from django.db.models import Q
from django.shortcuts import render

from movieapp.models import Movie


def SearchResult(request):
    movie = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = movie.objects.all().filter(Q(title__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'query': query, 'movies': movie})
