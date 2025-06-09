
from django.db import models
from Aplicaciones.Liga.models import Liga

# Create your models here.
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100, unique=True)  
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, related_name="equipos") 
    ciudad = models.CharField(max_length=50)
    anios_creacion = models.CharField(max_length = 20)
    escudo = models.FileField(upload_to='equipos', null=True, blank=True)
    ficha_tecnica = models.FileField(upload_to='equipos', null=True, blank=True)
    def __str__(self):
        return f"{self.nombre} ({self.liga.nombre})"

