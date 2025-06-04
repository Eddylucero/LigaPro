from django.shortcuts import render

# Create your views here.
def inicioLiga(request):
    return render(request, "inicioLiga.html")
