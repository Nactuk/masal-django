from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Masal
from dotenv import load_dotenv

load_dotenv()

def home(request):
    masallar = Masal.objects.all()
    context = {'masallar' : masallar}
    return render(request, "pages/home.html" , context)

# def detail(request, movie_id):
#     movie = get_object_or_404(Movie, pk = movie_id)
#     context = {'movie' : movie}
#     return render(request, "movies/detail.html", context)

def masallar(request):
    return render(request, "pages/masallar.html")