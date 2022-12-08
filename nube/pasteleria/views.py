from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import RequestContext
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from pasteleria.models import *
from pasteleria.forms import agregar
from prueba.models import *

def entrada(request):
    template="base.html"
    return render(request, template)

def hijo(request):
    templatesPasteleria="templ1.html"
    return render(request,  templatesPasteleria)

# Crea tus vistas aquí.
def listar(request):
    pasteleria1= pasteleria.objects.all()
    template="pasteleria/lista.html"
    context={
        'pasteleria': pasteleria1,

    }
    return render (request,template,context)

def crearpastel(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pasteleria/listar/')

    form = agregar 
    context={
        'form':form,

    }
    return render (request, "pasteleria/agregar.html", context)

def eliminarpastel(request, id):
    member= pasteleria.objects.get(id=id)
    member.delete()
    return redirect('pasteleria/listar/')

def actualizarpastel(request,id):
    if request.method=='POST':
        instance=pasteleria.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('pasteleria/listar/')
    
    dato = pasteleria.objects.get(id=id)
    template = 'pasteleria/actualizar.html'
    context = {
    'dato': dato,
    }
    return render(request, template, context)

  
  
  