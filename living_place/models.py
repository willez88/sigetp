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
## @namespace living_place.models
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
from base.models import (
    CommunalCouncil, ElectricService, SanitarySituation, TrashDisposal, LivingPlaceType,
    RoofType, WallType, FloorType, CementType, Valoration, Animal, Risk
)
from django.contrib.auth.models import User
from user.models import Pollster

# Create your models here.

class LivingPlace(models.Model):
    """!
    Clase que contiene los datos de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Fecha y hora del registro de la vivienda
    date_time = models.DateTimeField()

    ## Servicio eléctrico
    electric_service = models.ForeignKey(ElectricService,on_delete=models.CASCADE)

    ## Situación sanitaria
    sanitary_situation = models.ForeignKey(SanitarySituation,on_delete=models.CASCADE)

    ## Disposición de la basura
    trash_disposal = models.ForeignKey(TrashDisposal,on_delete=models.CASCADE)

    ## Tipo de la vivienda
    living_place_type = models.ForeignKey(LivingPlaceType,on_delete=models.CASCADE)

    ## Tipo del techo
    roof_type = models.ForeignKey(RoofType,on_delete=models.CASCADE)

    #Tipo de la pared
    wall_type = models.ForeignKey(WallType,on_delete=models.CASCADE)

    ## La pared está frizada o no
    wall_frieze = models.BooleanField(default=False)

    ## Tipo del piso
    floor_type = models.ForeignKey(FloorType,on_delete=models.CASCADE)

    ## Tipo del cemento del piso
    cement_type = models.ForeignKey(CementType,on_delete=models.CASCADE)

    ## Condición de la vivienda
    living_place_condition = models.ForeignKey(Valoration,on_delete=models.CASCADE)

    ## COndición del techo
    roof_condition = models.ForeignKey(
        Valoration,on_delete=models.CASCADE,
        related_name='roof_condition'
    )

    ## Condición de la pared
    wall_condition = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='wall_condition')

    ## Condición del piso
    floor_condition = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='floor_condition')

    ## Condición de la ventilación
    ventilation_condition = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='ventilation_condition')

    ## Condición de la iluminación
    ilumination_condition = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='ilumination_condition')

    ## Accesibilidad al ambulatorio
    ambulatory_accessibility = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='ambulatory')

    ## Accesibilidad a la escuela
    school_accessibility = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='school')

    ## Accesibilidad al liceo
    lyceum_accessibility = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='lyceum')

    ## Accesibilidad al centro de abastecimiento
    supply_center_accessibility = models.ForeignKey(Valoration,on_delete=models.CASCADE,related_name='supply_center')

    ## Número de habitaciones
    rooms_number = models.IntegerField()

    ## Número de salas
    living_rooms_number = models.IntegerField()

    ## Número de baños
    bathrooms_number = models.IntegerField()

    ## ¿Tiene terreno?
    has_terrain = models.BooleanField()

    ## Metros cuadrados del terreno
    square_meter = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)

    ## Terreno que está productivo
    productive = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)

    ## Terreno que está por producir
    non_productive = models.DecimalField(max_digits=18, decimal_places=2, default=0.0)

    ## Riesgo por río
    #river_risk = models.BooleanField()

    ## Riesgo por quebrada
    #gully_risk = models.BooleanField()

    ## Riesgo por derrumbe
    #landslides_risk = models.BooleanField()

    ## Riesgo por zona sísmica
    #seismic_zone_risk = models.BooleanField()

    ## Riesgo que presenta la vivienda
    risks = models.ManyToManyField(Risk)

    ## Animales que hay en la vivienda
    animals = models.ManyToManyField(Animal)

    ## Número de identificación de la vivienda
    living_place_number = models.CharField(max_length=20)

    ## Dirección exacta de la vivienda
    address = models.CharField(max_length=500)

    ## Coordenadas geográficas
    coordinate = models.CharField(max_length=255, blank=True)

    ## Observación
    observation = models.TextField()

    ## Establece la relación de la vivienda con el consejo comunal
    communal_council = models.ForeignKey(CommunalCouncil,on_delete=models.CASCADE)

    ## Establece la relación de la vivienda con el usuario
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 14-01-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el número de identificación y el id de la vivienda
        """

        return self.living_place_number + ' | ' + str(self.id)

class Photograph(models.Model):
    """!
    Clase que contiene los datos de imágenes de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Nombre de la imagen
    name = models.CharField(max_length=100)

    ## Nombre de la imagen
    picture = models.ImageField(upload_to='living_place/')

    ## Establece la relación de las imágenes con la vivienda
    living_place = models.ForeignKey(LivingPlace,on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 14-01-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Una cadena de caracteres con el nombre de la imagen
        """

        return self.photo