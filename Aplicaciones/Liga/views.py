from django.shortcuts import render, redirect
from .models import Liga
from django.contrib import messages
from django.conf import settings
import os

# Renderizar listado de ligas
def listarLigas(request):
    ligas = Liga.objects.all()  # Obtener todas las ligas
    return render(request, "Ligas/inicioLiga.html", {'ligas': ligas})

# Renderizar formulario para agregar una nueva liga
def nuevaLiga(request):
    return render(request, "Ligas/nuevaLiga.html")

# Almacenar datos de la liga en la BD
def guardarLiga(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        país = request.POST["pais"]
        temporada_actual = request.POST["temporada_actual"]

        logo = request.FILES.get("logo")
        reglamento = request.FILES.get("reglamento")

        Liga.objects.create(
            nombre=nombre, país=país, temporada_actual=temporada_actual,
            logo=logo, reglamento=reglamento
        )

        messages.success(request, "SE HA AGREGADO LA LIGA")
        return redirect('listarLigas')
    return redirect('listarLigas')

# Eliminar liga por ID
def eliminarLiga(request, id):
    ligaEliminar = Liga.objects.get(id=id)

    # Eliminar logo
    if ligaEliminar.logo:
        ruta_logo = os.path.join(settings.MEDIA_ROOT, ligaEliminar.logo.name)
        if os.path.isfile(ruta_logo):
            os.remove(ruta_logo)

    # Eliminar reglamento
    if ligaEliminar.reglamento:
        ruta_reglamento = os.path.join(settings.MEDIA_ROOT, ligaEliminar.reglamento.name)
        if os.path.isfile(ruta_reglamento):
            os.remove(ruta_reglamento)

    ligaEliminar.delete()
    messages.success(request, "SE HA ELIMINADO LA LIGA")
    return redirect('listarLigas')

# Renderizar formulario de edición de liga
def editarLiga(request, id):
    liga = Liga.objects.get(id=id)
    return render(request, "Ligas/editarLiga.html", {'liga': liga})

# Procesar la edición y actualizar en la BD
def procesarEdicionLiga(request, id):
    nombre = request.POST["nombre"]
    país = request.POST["pais"]
    temporada_actual = request.POST["temporada_actual"]

    liga = Liga.objects.get(id=id)
    liga.nombre = nombre
    liga.país = país
    liga.temporada_actual = temporada_actual

    # Procesando nuevo logo si se sube
    if "logo" in request.FILES:
        nuevo_logo = request.FILES.get("logo")
        if liga.logo:
            ruta_logo_antiguo = os.path.join(settings.MEDIA_ROOT, liga.logo.name)
            if os.path.isfile(ruta_logo_antiguo):
                os.remove(ruta_logo_antiguo)
        liga.logo = nuevo_logo

    # Procesando nuevo reglamento si se sube
    if "reglamento" in request.FILES:
        nuevo_reglamento = request.FILES.get("reglamento")
        if liga.reglamento:
            ruta_reglamento_antiguo = os.path.join(settings.MEDIA_ROOT, liga.reglamento.name)
            if os.path.isfile(ruta_reglamento_antiguo):
                os.remove(ruta_reglamento_antiguo)
        liga.reglamento = nuevo_reglamento

    liga.save()
    messages.success(request, "SE HA EDITADO LA LIGA")

    return redirect('listarLigas')
