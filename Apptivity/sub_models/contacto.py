# -*- coding: utf-8 -*-
import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()

import datetime
    
# Contacto model
class Contacto(models.Model):
    id: models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, default="")
    fecha_nacimiento = models.DateField()
    DNI = models.CharField(max_length=45, default="")
    tipo_DNI = models.CharField(max_length=45, default="")
    ciudad = models.CharField(max_length=10, default="")
    pais = models.IntegerField(default=57)
    fecha_creacion = models.DateField(default=datetime.date.today)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "contacto"

    def __str__(self):
        return self.nombre

    __repr__ = __str__

