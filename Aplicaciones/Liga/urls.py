from django.urls import path
from . import views

urlpatterns = [
    path('', views.listarLigas, name='listarLigas'),  
    path('nuevaLiga/', views.nuevaLiga, name='nuevaLiga'),  
    path('guardarLiga/', views.guardarLiga, name='guardarLiga'),  
    path('eliminarLiga/<int:id>/', views.eliminarLiga, name='eliminarLiga'),  
    path('editarLiga/<int:id>/', views.editarLiga, name='editarLiga'),
    path('procesarEdicionLiga/<int:id>/', views.procesarEdicionLiga, name='procesarEdicionLiga'),  
]
