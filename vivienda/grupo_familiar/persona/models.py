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
## @namespace persona.models
#
# Contiene las clases, atributos y métodos para los modelos a implementar en la aplicación persona
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
from base.constant import (
    SEXO, PARENTESCO, ESTADO_CIVIL, GRADO_INSTRUCCION, MISION_EDUCATIVA, TIPO_INGRESO, MISION_SOCIAL
)
from vivienda.grupo_familiar.models import GrupoFamiliar
import datetime

# Create your models here.

class Persona(models.Model):
    """!
    Clase que contiene los datos de las personas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Nombre de la Persona
    nombre = models.CharField(max_length=100)

    ## Apellido de la Persona
    apellido = models.CharField(max_length=100)

    ## Cédula de la Persona. Si tiene o no
    cedula = models.CharField(
        max_length=9,
        unique=True,
        null=True
    )

    # +058-416-0708340
    telefono = models.CharField(
        max_length=18,
    )

    ## Establece el correo de la persona
    correo = models.CharField(
        max_length=100, help_text=("correo@correo.com")
    )

    ## Establece el sexo de la Persona
    sexo = models.CharField(max_length=1, choices=SEXO)

    ## Establece la fecha de nacimiento de la Persona
    fecha_nacimiento = models.DateField()

    ## Establece el parentesto que tiene el jefe familiar con el resto del Grupo Familiar
    parentesco = models.CharField(max_length=2, choices=PARENTESCO)

    ## Estalece si la persona es jefe familiar o no
    jefe_familiar = models.BooleanField()

    ## Establece el Estado Civil de la Persona
    estado_civil = models.CharField(max_length=2, choices=ESTADO_CIVIL)

    ## Establece el Grado de Instrucción de la Persona
    grado_instruccion = models.CharField(max_length=2, choices=GRADO_INSTRUCCION)

    ## Establece la Misión Educativa que tiene la Persona
    mision_educativa = models.CharField(max_length=2, choices=MISION_EDUCATIVA)

    ## Establece la Misión Social ue tiene la Persona
    mision_social = models.CharField(max_length=2, choices=MISION_SOCIAL)

    ## Establece la Profesión de la Persona (sin categoria de momento)
    profesion = models.CharField(max_length=100)

    ## Establece la Ocupación de la Persona (sin categoria de momento)
    ocupacion = models.CharField(max_length=100)

    ## Establece el Lugar de trabajo de la persona
    lugar_trabajo = models.CharField(max_length=100)

    ## Establece los ingresos de dinero de la Persona
    ingreso = models.CharField(max_length=100, choices=TIPO_INGRESO)

    ## Establece si la persona tiene o no ingresos por ser pensionado
    pensionado = models.BooleanField()

    ## Establece si la persona tiene o no ingresos por ser jubilado
    jubilado = models.BooleanField()

    ## Establece el Deporte que practica la Persona (sin categoria de momento)
    deporte = models.CharField(max_length=100)

    ## Establece la Enfermedad que presenta la Persona
    enfermedad = models.CharField(max_length=500)

    ## Establece la Discapacidad que tiene la Persona
    discapacidad = models.CharField(max_length=500)

    ## Establece si la Persona ha leido la ley de los consejos comunales
    ley_consejo_comunal = models.BooleanField(default=False)

    ## Establece que cursos le gustaría hacer a la Persona (sin categoria de momento)
    curso = models.CharField(max_length=100)

    ## Establece todas las organizaciones que la Persona conoce (las preguntas de arriba se redondean en esta)
    organizacion_comunitaria = models.CharField(max_length=500)

    ## Estable que hace la Persona en sus horas de ocio
    ocio = models.CharField(max_length=500)

    ## Estable la sugerencia que la Persona ofrece para poder mejorar la Comunicación en la Comunidad
    mejorar_comunicacion = models.CharField(max_length=500)

    ## Establece la Inseguridad que la Persona considera que hay en la comunidad
    inseguridad = models.CharField(max_length=500)

    ## Establece algún comentario que la Persona quiera hacer en relación a las necesidades de la comunidad
    comentario = models.CharField(max_length=500)

    ## Establece alguna observación que se tenga sobre la persona
    observacion = models.TextField()

    ## Establece la relación con el grupo familiar
    grupo_familiar = models.ForeignKey(GrupoFamiliar,on_delete=models.CASCADE)

    ## Cacula la edad en años que tiene una persona según su fecha de nacimiento
    def edad(self):
        """!
        Método que calcula la edad de la persona

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un número entero que representa la edad
        """

        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25  )

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 14-01-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre, apellido y cédula de la persona
        """

        return self.nombre + ' ' + self.apellido + ', ' + str(self.cedula)
