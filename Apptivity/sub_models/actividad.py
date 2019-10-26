# -*- coding: utf-8 -*-
import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()
    
from .contacto import Contacto
import datetime

# Actividad model
class Actividad(models.Model):
    id: models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, default="")
    descripcion = models.CharField(max_length=250, default="")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.CharField(max_length=250, default="")
    tipo = models.CharField(max_length=10, default="") ##principal or secundario
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(default=datetime.date.today)
    contactos = models.ManyToManyField(Contacto,"actividades_contactos")

    class Meta:
        db_table = "actividad"

    def __str__(self):
        return self.nombre

    __repr__ = __str__