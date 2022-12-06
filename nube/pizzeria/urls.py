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
    path('pizza/listarpizza/',listarpizza,name="pizza/listarpizza"),
    path('pizza/crearpizza', nuevapizza, name='pizza/crearpizza'),
    path('eliminarpizza/<int:id>',eliminarpizza,name='eliminarpizza'),
    path('/actualizarpizza/<int:id>',actualizarpizza,name='/actualizarpizza/'),
]