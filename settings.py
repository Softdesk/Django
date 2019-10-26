# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:11:59 2019

@author: E201
"""

DATABASES = {
    'default': {
        'NAME': 'demo',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'estudiante',
        'HOST':'localhost',
        'PORT': '3306',
        'OPTIONS': {
          'autocommit': True,
          'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}
        
INSTALLED_APPS = (
    'Apptivity',
)

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = '6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa'