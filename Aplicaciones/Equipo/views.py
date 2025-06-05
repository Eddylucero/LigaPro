from django.shortcuts import render, redirect
from .models import Equipo
from Aplicaciones.Liga.models import Liga
from django.contrib import messages
from django.conf import settings
import os

# Renderizar listado de equipos
def listarEquipos(request):
    equipos = Equipo.objects.select_related('liga').all()  # Optimización con select_related
    return render(request, "Equipos/inicioEquipo.html", {'equipos': equipos})

# Renderizar formulario para agregar un nuevo equipo
def nuevoEquipo(request):
    ligas = Liga.objects.all()  # Obtener todas las ligas disponibles
    return render(request, "Equipos/nuevoEquipo.html", {'ligas': ligas})

# Almacenar datos del equipo en la BD
def guardarEquipo(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        liga_id = request.POST["liga"]
        ciudad = request.POST["ciudad"]

        escudo = request.FILES.get("escudo")
        ficha_tecnica = request.FILES.get("ficha_tecnica")

        liga = Liga.objects.get(id=liga_id)
        Equipo.objects.create(
            nombre=nombre, liga=liga, ciudad=ciudad,
            escudo=escudo, ficha_tecnica=ficha_tecnica
        )

        messages.success(request, "SE HA AGREGADO EL EQUIPO")
        return redirect('listarEquipos')
    return redirect('listarEquipos')

# Eliminar equipo por ID
def eliminarEquipo(request, id):
    equipoEliminar = Equipo.objects.get(id=id)

    if equipoEliminar.escudo:
        ruta_escudo = os.path.join(settings.MEDIA_ROOT, equipoEliminar.escudo.name)
        if os.path.isfile(ruta_escudo):
            os.remove(ruta_escudo)
    
    if equipoEliminar.ficha_tecnica:
        ruta_ficha = os.path.join(settings.MEDIA_ROOT, equipoEliminar.ficha_tecnica.name)
        if os.path.isfile(ruta_ficha):
            os.remove(ruta_ficha)

    equipoEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL EQUIPO")
    return redirect('listarEquipos')

# Renderizar formulario de edición de equipo
def editarEquipo(request, id):
    equipo = Equipo.objects.get(id=id)
    ligas = Liga.objects.all()  # Obtener todas las ligas disponibles
    return render(request, "Equipos/editarEquipo.html", {'equipo': equipo, 'ligas': ligas})

# Procesar la edición y actualizar en la BD
def procesarEdicionEquipo(request, id):
    nombre = request.POST["nombre"]
    liga_id = request.POST["liga"]
    ciudad = request.POST["ciudad"]

    equipo = Equipo.objects.get(id=id)
    equipo.nombre = nombre
    equipo.liga = Liga.objects.get(id=liga_id)
    equipo.ciudad = ciudad

    if "escudo" in request.FILES:
        nuevo_escudo = request.FILES.get("escudo")
        if equipo.escudo:
            ruta_escudo_antiguo = os.path.join(settings.MEDIA_ROOT, equipo.escudo.name)
            if os.path.isfile(ruta_escudo_antiguo):
                os.remove(ruta_escudo_antiguo)
        equipo.escudo = nuevo_escudo

    if "ficha_tecnica" in request.FILES:
        nueva_ficha = request.FILES.get("ficha_tecnica")
        if equipo.ficha_tecnica:
            ruta_ficha_antigua = os.path.join(settings.MEDIA_ROOT, equipo.ficha_tecnica.name)
            if os.path.isfile(ruta_ficha_antigua):
                os.remove(ruta_ficha_antigua)
        equipo.ficha_tecnica = nueva_ficha

    equipo.save()
    messages.success(request, "SE HA EDITADO EL EQUIPO")

    return redirect('listarEquipos')
