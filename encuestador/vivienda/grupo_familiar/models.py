from django.db import models
from base.constant import TIPO_TENENCIA
from encuestador.vivienda.models import Vivienda
# Create your models here.

class GrupoFamiliar(models.Model):
    apellido_familia = models.CharField(max_length=100)
    familia_beneficiada = models.BooleanField(default=False)
    tenencia = models.CharField(max_length=2, choices=TIPO_TENENCIA)
    alquilada = models.FloatField()
    pasaje = models.BooleanField(default=False)
    vivienda = models.ForeignKey(Vivienda)
