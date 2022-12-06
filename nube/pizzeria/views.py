from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from pizzeria.models import *
from pizzeria.forms import agregar
from .views import *
#from prueba.models import *


def entrada(request):
    templates="base.html"
    return render(request, templates)

def hijo(request):
    templates="templ1.html"
    return render(request, templates)

# Create your views here.
def listarpizza(request):
    pizza1= pizza.objects.all()
    template="pizza/listarpizza.html"
    context={
        'pizza': pizza1,

    }
    return render (request,template,context)

def nuevapizza(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/pizza/listarpizza.html")

    form = agregar 
    context={
        'form':form,

    }
    return render (request, "agregar.html", context)


def eliminarpizza(request, id):
    member= pizza.objects.get(id=id)
    member.delete()
    return redirect('pizza/listarpizza')

def actualizarpizza(request, id):
    if request.method=='POST':
        instance=pizza.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/pizza/listarpizza')
    dato = pizza.objects.get(id=id)
    templatespiiza = 'actualizar.html'
    context = {
    'dato': dato,
    }
    return render(request, templatespiiza, context)

  
  
  