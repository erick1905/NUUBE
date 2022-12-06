from django.db import models
from  django.conf import settings



# Create your models here.
class pasteleria(models.Model):
    #tipopastel = models.CharField(max_length=20, help_text="Enter field documentation")
    tipopastel=models.CharField(max_length=20, blank=True, null=True)
    tamano= models.CharField(max_length=20, blank=True, null=True)
    #Descripcion= models.IntegerField(max_length=20, blank=True, null=True)
    precio=models.CharField(max_length=20, blank=True, null=True)