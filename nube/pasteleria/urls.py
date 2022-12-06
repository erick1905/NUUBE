from django.contrib import admin
from django.urls import path
#from .views import*
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from .views import *


urlpatterns = [
    path('pasteleria/listar/',listar,name="pasteleria/listar/"),
    path('pasteleria/crear/', pasteleriacrear, name='pasteleria/crear'),
    path('Eliminar/<int:id>',eliminar,name='Eliminar'),
    path('sactualizar/<int:id>',actualizar,name='actualizar'),
]