"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CENDITEL (2017)

Autores: William Páez

La Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres (CENDITEL),
ente adscrito al Ministerio del Poder Popular para Educación Universitaria, Ciencia y Tecnología
(MPPEUCT), concede permiso para usar, copiar, modificar y distribuir libremente y sin fines
comerciales el "Software - Registro de bienes de CENDITEL", sin garantía
alguna, preservando el reconocimiento moral de los autores y manteniendo los mismos principios
para las obras derivadas, de conformidad con los términos y condiciones de la licencia de
software de la Fundación CENDITEL.

El software es una creación intelectual necesaria para el desarrollo económico y social
de la nación, por tanto, esta licencia tiene la pretensión de preservar la libertad de
este conocimiento para que contribuya a la consolidación de la soberanía nacional.

Cada vez que copie y distribuya el "Software - Registro de bienes de CENDITEL"
debe acompañarlo de una copia de la licencia. Para más información sobre los términos y condiciones
de la licencia visite la siguiente dirección electrónica:
http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/
"""
## @namespace vivienda.models
#
# Contiene las clases, atributos y métodos para los modelos a implementar en la aplicación vivienda
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.db import models
from base.constant import (TIPO_VIVIENDA, TIPO_TECHO, TIPO_PARED, TIPO_PISO, VALORACION, TIPO_CEMENTO, SERVICIO_ELECTRICO,
    SITUACION_SANITARIA, DISPOSICION_BASURA
)
from base.models import ConsejoComunal
from django.contrib.auth.models import User

# Create your models here.

class Vivienda(models.Model):
    """!
    Clase que contiene los datos de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

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
    """!
    Clase que contiene los datos de imágenes de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Nombre de la imagen
    nombre = models.CharField(max_length=100)

    ## Imagen cifrada en base64
    imagen_base64 = models.TextField()

    ## Establece la relación de las imágenes con la vivienda
    vivienda = models.ForeignKey(Vivienda,on_delete=models.CASCADE)
