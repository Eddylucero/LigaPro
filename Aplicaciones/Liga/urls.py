from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioLiga, name='inicioLiga'),
]
