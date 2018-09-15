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
## @namespace family_group.models
#
# Contiene las clases, atributos y métodos para los modelos a implementar en la aplicación grupo_familiar
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.db import models
from django.utils.translation import ugettext_lazy as _
from base.models import TenureType
from living_place.models import LivingPlace
# Create your models here.

class FamilyGroup(models.Model):
    """!
    Clase que contiene los datos de los grupos familiares

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Apellido del grupo familiar
    family_last_name = models.CharField(max_length=100)

    ## Familia beneficiada por clap
    beneficiary_family = models.BooleanField(default=False)

    ## Tenencia que el grupo familiar tiene sobre la vivienda
    tenure = models.ForeignKey(TenureType,on_delete=models.CASCADE)

    ## Alquiler de la vivienda en meses
    rented = models.IntegerField(default=0)

    ## Consulta sobre el pasaje
    ticket = models.BooleanField(default=False)

    ## Observación
    observation = models.TextField()

    ## Establece la relación del grupo familiar con la vivienda
    living_place = models.ForeignKey(LivingPlace,on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 14-01-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el apellido de la familia y el id del grupo familiar
        """

        return self.family_last_name + ' | ' + str(self.id)

    class Meta:
        verbose_name = _('Grupo Familiar')
        verbose_name_plural = _('Grupos Familiares')