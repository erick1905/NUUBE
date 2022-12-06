from  ninja import Router 
router = Router()
from .models import *

@router.post("/agregar")
def insertar(request,color):
    a=pizza.create(color)
    return "ha sido agregado exitosamente"