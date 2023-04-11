from django.db import models

class Incidencia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=10)
    remove = models.BooleanField()