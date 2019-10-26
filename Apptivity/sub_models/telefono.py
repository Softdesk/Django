import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()
    
from .contacto import Contacto
import datetime

# Telefono model
class Telefono(models.Model):
    id: models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=10, default="")
    tipo = models.CharField(max_length=10, default="") ##principal or secundario
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(default=datetime.date.today)
    contacto = models.ForeignKey(Contacto,default=1, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "telefono"