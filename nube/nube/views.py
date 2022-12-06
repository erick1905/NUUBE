from django.shortcuts import render
from django.shortcuts import redirect
#from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from prueba.models import *

def entrada(request):
    template="base.html"
    return render(request, template)

def hijo(request):
    template="templ1.html"
    return render(request, template)

