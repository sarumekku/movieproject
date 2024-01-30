from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {'mlist': movie}
    return render(request, 'index.html', context)


def details(request, movie_id):
    result = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': result})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )

        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, img=img)
        movie.save()
        return redirect('/')

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
