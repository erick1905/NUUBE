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
     path('pasteleria/crearpastel/', crearpastel, name='crearpastel/'),
    path('eliminarpastel/<int:id>',eliminarpastel,name='eliminarpastel'),
    path('actualizarpastel/<int:id>',actualizarpastel,name='actualizarpastel/'),
]