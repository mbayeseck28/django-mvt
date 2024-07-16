# from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render



def index(request):
    date = datetime.today()
    return render(request, "DocBlog/index.html", context={"prenom": "Mbaye", "date": date})
    # return HttpResponse("<h1>Bonjour, Bienvenue sur mon site</h1>")