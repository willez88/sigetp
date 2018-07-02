"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CIDA (2017)

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
from base.constant import (
    TIPO_VIVIENDA, TIPO_TECHO, TIPO_PARED, TIPO_PISO, VALORACION,
    TIPO_CEMENTO, SERVICIO_ELECTRICO, SITUACION_SANITARIA, DISPOSICION_BASURA
)
from base.models import CommunalCouncil
from django.contrib.auth.models import User
from usuario.models import Pollster

# Create your models here.

class Vivienda(models.Model):
    """!
    Clase que contiene los datos de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Fecha y hora del registro de la vivienda
    fecha_hora = models.DateTimeField()

    ## Servicio eléctrico
    servicio_electrico = models.CharField(max_length=2, choices=SERVICIO_ELECTRICO)

    ## Situación sanitaria
    situacion_sanitaria = models.CharField(max_length=2, choices=SITUACION_SANITARIA)

    ## Disposición de la basura
    disposicion_basura = models.CharField(max_length=2, choices=DISPOSICION_BASURA)

    ## Tipo de la vivienda
    tipo_vivienda = models.CharField(max_length=2, choices=TIPO_VIVIENDA)

    ## Tipo del techo
    tipo_techo = models.CharField(max_length=2, choices=TIPO_TECHO)

    #Tipo de la pared
    tipo_pared = models.CharField(max_length=2, choices=TIPO_PARED)

    ## La pared está frizada o no
    pared_frizada = models.BooleanField(default=False)

    ## Tipo del piso
    tipo_piso = models.CharField(max_length=2, choices=TIPO_PISO)

    ## Tipo del cemento del piso
    tipo_cemento = models.CharField(max_length=2, choices=TIPO_CEMENTO)

    ## Condición de la vivienda
    condicion_vivienda = models.CharField(max_length=1, choices=VALORACION)

    ## COndición del techo
    condicion_techo = models.CharField(max_length=1, choices=VALORACION)

    ## Condición de la pared
    condicion_pared = models.CharField(max_length=1, choices=VALORACION)

    ## Condición del piso
    condicion_piso = models.CharField(max_length=1, choices=VALORACION)

    ## Condición de la ventilación
    condicion_ventilacion = models.CharField(max_length=1, choices=VALORACION)

    ## Condición de la iluminación
    condicion_iluminacion = models.CharField(max_length=1, choices=VALORACION)

    ## Accesibilidad al ambulatorio
    accesibilidad_ambulatorio = models.CharField(max_length=1, choices=VALORACION)

    ## Accesibilidad a la escuela
    accesibilidad_escuela = models.CharField(max_length=1, choices=VALORACION)

    ## Accesibilidad al liceo
    accesibilidad_liceo = models.CharField(max_length=1, choices=VALORACION)

    ## Accesibilidad al centro de abastecimiento
    accesibilidad_centro_abastecimiento = models.CharField(max_length=1, choices=VALORACION)

    ## Número de habitaciones
    numero_habitaciones = models.IntegerField()

    ## Número de salas
    numero_salas = models.IntegerField()

    ## Número de baños
    numero_banhos = models.IntegerField()

    ## ¿Tiene terreno?
    tiene_terreno = models.BooleanField()

    ## Metros cuadrados del terreno
    metro_cuadrado = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)

    ## Terreno que está productivo
    productivo = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)

    ## Terreno que está por producir
    por_producir = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)

    ## Riesgo por río
    riesgo_rio = models.BooleanField()

    ## Riesgo por quebrada
    riesgo_quebrada = models.BooleanField()

    ## Riesgo por derrumbe
    riesgo_derrumbe = models.BooleanField()

    ## Riesgo por zona sísmica
    riesgo_zona_sismica = models.BooleanField()

    ## Animales que hay en la vivienda
    animales = models.CharField(max_length=500)

    ## Número de identificación de la vivienda
    numero_vivienda = models.CharField(max_length=20)

    ## Dirección exacta de la vivienda
    direccion = models.CharField(max_length=500)

    ## Coordenadas geográficas
    coordenadas = models.CharField(max_length=255, blank=True)

    ## Observación
    observacion = models.TextField()

    ## Establece la relación de la vivienda con el consejo comunal
    communal_council = models.ForeignKey(CommunalCouncil,on_delete=models.CASCADE)

    ## Establece la relación de la vivienda con el usuario
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    ## Establece la relación entre el encuestador y la vivienda
    #pollster = models.ForeignKey(Pollster,on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 14-01-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el número de identificación y el id de la vivienda
        """

        return self.numero_vivienda + ' | ' + str(self.id)

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

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 14-01-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la imagen
        """

        return self.nombre
