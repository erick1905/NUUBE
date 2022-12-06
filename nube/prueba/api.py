from  ninja import Router 
router = Router()
from .models import *

@router.get("/home")
def home (request):
    return "hola que tal te esta contestando la API"

@router.get("/estatura")
def estatura(request, altura):
    return f"la altura aproximada de juan es {altura}m "

@router.post("/agregar")
def insertar(request,color):
    a=carro.create(color)
    return "ha sido agregado exitosamente"