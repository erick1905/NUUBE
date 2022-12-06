from  ninja import Router 
router = Router()
from .models import *

@router.post("/agregar")
def insertar(request,pasteleria):
    a=pasteleria.create(pasteleria)
    return "ha sido agregado exitosamente"