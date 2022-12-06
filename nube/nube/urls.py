"""nube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import*
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include

from ninja import NinjaAPI
from prueba.api import router as api_router
from pasteleria.api import router as api_router
from pizzeria.api import router as api_router
api= NinjaAPI()
api.add_router("/api/",api_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',entrada, name="entrada"),
    path('hijo/',hijo, name="hijo"),
    url(r'^', include('prueba.urls')),
    url(r'^', include('pizzeria.urls')),
    url(r'^', include('pasteleria.urls')),
    #path("api/",api.urls),
]


#if settings.MEDIA_URL.startswith("/"):
#   urlpatterns += [
 #       url(
  #          r'^{MEDIA_URL}(?P<path>.*)$'.format(MEDIA_URL=re.escape(settings.MEDIA_URL.lstrip('/'))),
   #         serve,
    #        {'document_root': settings.MEDIA_ROOT},
     #   ),
    #]
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
