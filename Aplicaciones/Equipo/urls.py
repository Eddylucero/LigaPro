from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarEquipos, name='listarEquipos'),  
    path('nuevoEquipo/', views.nuevoEquipo, name='nuevoEquipo'),  
    path('guardarEquipo/', views.guardarEquipo, name='guardarEquipo'),  
    path('eliminarEquipo/<int:id>/', views.eliminarEquipo, name='eliminarEquipo'),  
    path('editarEquipo/<int:id>/', views.editarEquipo, name='editarEquipo'),  
    path('procesarEdicionEquipo/<int:id>/', views.procesarEdicionEquipo, name='procesarEdicionEquipo'),  
]
