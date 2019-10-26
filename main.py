# -*- coding: utf-8 -*-
    
# Turn off bytecode generation
import sys
import datetime
sys.dont_write_bytecode = True

# Django specific settings
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

# Import your models for use in your script
from Apptivity.models import *

#Create Contacto
contacto = Contacto()
contacto.nombre = 'Jhon Murillo'
contacto.fecha_nacimiento= datetime.date(1991, 9, 9)
contacto.DNI='123'
contacto.tipo_DNI='CC'
contacto.ciudad='13001'
contacto.pais=57
contacto.save()

#Create Email
email = Email()
email.correo = 'jmurillo@gmail.com'
email.tipo='PRINCIPAL'
email.contacto=contacto
email.save()

email2 = Email()
email2.correo = 'jmurillo2@gmail.com'
email2.tipo='SECUNDARIO'
email2.contacto=contacto
email2.save()

print('Contacto Creado...')
#Create Actividad
actividad = Actividad()
actividad.nombre = 'English Class'
actividad.descripcion = 'Aprendier Ingles'
actividad.fecha_inicio= datetime.date(2019, 9, 9)
actividad.fecha_fin= datetime.date(2019, 10, 9)
actividad.ubicacion='Cartagena'
actividad.tipo='CURRICULAR'
actividad.save()

print('Actividad Creada...')

actividad.contactos.add(contacto)

print('Contacto: ', contacto.nombre, ' Asociado a la actividad: ',actividad.nombre )
