from django.db import models

class Liga(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100, unique=True)  
    pais = models.CharField(max_length=50)  
    temporada_actual = models.CharField(max_length=20)  
    logo = models.FileField(upload_to='ligas', null=True, blank=True)  
    reglamento = models.FileField(upload_to='ligas', null=True, blank=True)  

    def __str__(self):
        return self.nombre
