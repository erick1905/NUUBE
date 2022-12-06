from django.db import models
from  django.conf import settings


# Create your models here.
class pizza(models.Model):
    tipopizza=models.CharField(max_length=20, blank=True, null=True)
    tamano= models.CharField(max_length=20, blank=True, null=True)
    #extras= models.IntegerField(max_length=20, blank=True, null=True)
    precio=models.CharField(max_length=20, blank=True, null=True)