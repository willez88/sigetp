from django.db import models
from base.constant import (TIPO_VIVIENDA, TIPO_TECHO, TIPO_PARED, TIPO_PISO, VALORACION, TIPO_CEMENTO, SERVICIO_ELECTRICO,
    SITUACION_SANITARIA, DISPOSICION_BASURA
)
from base.models import ConsejoComunal
from django.contrib.auth.models import User

# Create your models here.

class Vivienda(models.Model):
    fecha_hora = models.DateTimeField()
    servicio_electrico = models.CharField(max_length=2, choices=SERVICIO_ELECTRICO)
    situacion_sanitaria = models.CharField(max_length=2, choices=SITUACION_SANITARIA)
    disposicion_basura = models.CharField(max_length=2, choices=DISPOSICION_BASURA)
    tipo_vivienda = models.CharField(max_length=2, choices=TIPO_VIVIENDA)
    tipo_techo = models.CharField(max_length=2, choices=TIPO_TECHO)
    tipo_pared = models.CharField(max_length=2, choices=TIPO_PARED)
    pared_frizada = models.BooleanField(default=False)
    tipo_piso = models.CharField(max_length=2, choices=TIPO_PISO)
    tipo_cemento = models.CharField(max_length=2, choices=TIPO_CEMENTO)
    condicion_vivienda = models.CharField(max_length=1, choices=VALORACION)
    condicion_techo = models.CharField(max_length=1, choices=VALORACION)
    condicion_pared = models.CharField(max_length=1, choices=VALORACION)
    condicion_piso = models.CharField(max_length=1, choices=VALORACION)
    condicion_ventilacion = models.CharField(max_length=1, choices=VALORACION)
    condicion_iluminacion = models.CharField(max_length=1, choices=VALORACION)
    accesibilidad_ambulatorio = models.CharField(max_length=1, choices=VALORACION)
    accesibilidad_escuela = models.CharField(max_length=1, choices=VALORACION)
    accesibilidad_liceo = models.CharField(max_length=1, choices=VALORACION)
    accesibilidad_centro_abastecimiento = models.CharField(max_length=1, choices=VALORACION)
    numero_habitaciones = models.IntegerField()
    numero_salas = models.IntegerField()
    numero_banhos = models.IntegerField()
    tiene_terreno = models.BooleanField()
    metro_cuadrado = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    productivo = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    por_producir = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)
    riesgo_rio = models.BooleanField()
    riesgo_quebrada = models.BooleanField()
    riesgo_derrumbe = models.BooleanField()
    riesgo_zona_sismica = models.BooleanField()
    animales = models.CharField(max_length=500)
    numero_vivienda = models.CharField(max_length=20)
    direccion = models.CharField(max_length=500)
    coordenadas = models.CharField(max_length=255, blank=True)
    observacion = models.TextField()
    consejo_comunal = models.ForeignKey(ConsejoComunal,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Imagen(models.Model):
    nombre = models.CharField(max_length=100)
    imagen_base64 = models.TextField()
    vivienda = models.ForeignKey(Vivienda,on_delete=models.CASCADE)
