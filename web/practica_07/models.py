from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Grupo(models.Model):
    nombre = models.CharField(primary_key=True, max_length=30)
    fecha_fundacion = models.DateField(default=timezone.now, blank=True)
    estilo = models.CharField(max_length=30, blank=True)

    def get_all_objects(self):
        queryset = self.__class__.objects.all()

        return queryset
    
class Musico(models.Model):
    dni = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=60, blank=True)
    fecha_nacimiento = models.DateField(default=timezone.now, blank=True)
    instrumento_principal = models.CharField(max_length=20, blank=True)
    grupos = models.ManyToManyField(Grupo)

class Album(models.Model):
    titulo = models.CharField(primary_key=True, max_length=40)
    distribuidora = models.CharField(max_length=30, blank=True)
    fecha_lanzamiento = models.DateField(default=timezone.now, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
