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
## @namespace usuario.models
#
# Contiene las clases, atributos y métodos para los modelos a implementar en la aplicación usuario
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import User
from base.models import CommunalCouncil
from base.constant import LEVEL

# Create your models here.

class Profile(models.Model):
    """!
    Clase que contiene los datos del perfil de un usuario

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Número telefónico del usuario
    phone = models.CharField(
        max_length=16,
    )

    ## Nivel del usuario
    level = models.IntegerField(choices=LEVEL)

    ## Establece la relación entre el perfil y el user
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )

    ## Establece la relación del consejo comunal con el perfil del usuario
    #consejo_comunal = models.ForeignKey(ConsejoComunal,on_delete=models.CASCADE)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfiles")
        ordering = ("user",)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre y apellido del usuario
        """

        return "%s, %s" % (self.user.first_name, self.user.last_name)

class Communal(models.Model):
    """!
    Clase que contiene los datos de un usuario del nivel consejo comunal

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 19-06-2018
    """

    ## Establece la relación entre el modelo ConsejoComunal y el modelo Comunal
    communal_council = models.OneToOneField(
        CommunalCouncil, on_delete=models.CASCADE
    )

    ## Establece la relación entre el modelo Perfil y el modelo Comunal
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE
    )

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 19-06-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre, apellido del usuario y el consejo comunal que administra
        """

        return "%s %s | %s" % (self.profile.user.first_name, self.profile.user.last_name, self.communal_council)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 28-06-2018
        """

        verbose_name = _("Nivel Consejo Comunal")
        verbose_name_plural = _("Nivel Consejos Comunales")

class Pollster(models.Model):
    """!
    Clase que contiene los datos del perfil de un usuario del nivel encuestador

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 19-06-2018
    """

    communal = models.ForeignKey(
        Communal, on_delete=models.CASCADE
    )

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE
    )

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 19-06-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre y apellido del usuario
        """

        return "%s %s" % (self.communal.profile.user.first_name, self.communal.profile.user.last_name)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 28-06-2018
        """

        verbose_name = _("Encuestador")
        verbose_name_plural = _("Encuestadores")
