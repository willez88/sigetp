from django.db import models
from base.constant import TIPO_TENENCIA
from vivienda.models import Vivienda
# Create your models here.

class GrupoFamiliar(models.Model):
    apellido_familia = models.CharField(max_length=100)
    familia_beneficiada = models.BooleanField(default=False)
    tenencia = models.CharField(max_length=2, choices=TIPO_TENENCIA)
    alquilada = models.IntegerField(default=0)
    pasaje = models.BooleanField(default=False)
    observacion = models.TextField()
    vivienda = models.ForeignKey(Vivienda,on_delete=models.CASCADE)
