from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')
def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})
def list_movie_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movies_list':movies_list})
