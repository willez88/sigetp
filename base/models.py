"""
Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP)

Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @namespace base.models
#
# Contiene las clases, atributos y métodos para el modelo de datos básico
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators

class Pais(models.Model):

    ## Nombre del pais
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estado(models.Model):

    ## Nombre del Estado
    nombre = models.CharField(max_length=50)

    ## Pais en donde esta ubicado el Estado
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):

    ## Nombre del Municipio
    nombre = models.CharField(max_length=50)

    ## Estado en donde se encuentra el Municipio
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Parroquia(models.Model):

    ## Nombre de la Parroquia
    nombre = models.CharField(max_length=50)

    ## Municipio en el que se encuentra ubicada la Parroquia
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):

    ## Nombre de la Ciudad
    nombre = models.CharField(max_length=50)

    ## Estado en donde se encuentra ubicada la Ciudad
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class ConsejoComunal(models.Model):

    ## Número de rif del Consejo Comunal
    rif = models.CharField(
        max_length=10, help_text=_("Rif del Consejo Comunal"),
        validators=[
            validators.RegexValidator(
                r'^C[\d]{9}$',
                _("Introduzca un rif válido. Solo se permite la letra C, números y una longitud de 10 carácteres.")
            ),
        ],
        primary_key=True
    )

    ## Nombre del Consejo Comunal
    nombre = models.CharField(max_length=500)

    ## Parroquia en el que se encuetra ubicado el Consejo Comunal
    parroquia = models.ForeignKey(Parroquia,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("Consejo Comunal")
        verbose_name_plural = _("Consejos Comunales")
