from django.shortcuts import render
from .models import carro
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms 
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def listar(request):
    carros= carro.objects.all()
    template="listar.html"
    context={
        'carros': carros,

    }
    return render (request,template,context)

def carrocrear(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')

    form = agregar 
    context={
        'form':form,

    }
    return render (request, "agregar.html", context)
def eliminar(request, id):
  member = carro.objects.get(id=id)
  member.delete()
  return redirect(reverse('listar'))

def actualizar(request, id):
    if request.method=='POST':
        instance=carro.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('listar')
    
    dato = carro.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'actualizar.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)

  
  
  

  
  
  