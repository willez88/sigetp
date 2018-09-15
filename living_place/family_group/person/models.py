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
## @namespace person.models
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
from base.models import (
    Sex, FamilyRelationship, MaritalStatus, InstructionDegree, EducationalMission, SocialMission,
    Profession, Occupation, IncomeType, Sport, Disease, Disability, Course, CommunityOrganization,
    Workplace
)
from living_place.family_group.models import FamilyGroup
import datetime

# Create your models here.

class Person(models.Model):
    """!
    Clase que contiene los datos de las personas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Nombre de la Persona
    first_name = models.CharField(max_length=100)

    ## Apellido de la Persona
    last_name = models.CharField(max_length=100)

    ## Cédula de la Persona. Si tiene o no
    identity_card = models.CharField(
        max_length=9,
        unique=True,
        null=True
    )

    # +058-416-0708340
    phone = models.CharField(
        max_length=18,
    )

    ## Establece el correo de la persona
    email = models.CharField(
        max_length=100, help_text=("correo@correo.com")
    )

    ## Establece el sexo de la Persona
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)

    ## Establece la fecha de nacimiento de la Persona
    birthdate = models.DateField()

    ## Establece el parentesto que tiene el jefe familiar con el resto del Grupo Familiar
    family_relationship = models.ForeignKey(FamilyRelationship, on_delete=models.CASCADE)

    ## Estalece si la persona es jefe familiar o no
    family_head = models.BooleanField()

    ## Establece el Estado Civil de la Persona
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)

    ## Establece el Grado de Instrucción de la Persona
    instruction_degree = models.ForeignKey(InstructionDegree, on_delete=models.CASCADE)

    ## Establece la Misión Educativa que tiene la Persona
    educational_mission = models.ForeignKey(EducationalMission, on_delete=models.CASCADE)

    ## Establece la Misión Social ue tiene la Persona
    social_mission = models.ForeignKey(SocialMission, on_delete=models.CASCADE)

    ## Establece la Profesión de la Persona (sin categoria de momento)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    ## Establece la Ocupación de la Persona (sin categoria de momento)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)

    ## Establece el Lugar de trabajo de la persona
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE)

    ## Establece los ingresos de dinero de la Persona
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)

    ## Establece si la persona tiene o no ingresos por ser pensionado
    pensioner = models.BooleanField()

    ## Establece si la persona tiene o no ingresos por ser jubilado
    retired = models.BooleanField()

    ## Establece el Deporte que practica la Persona (sin categoria de momento)
    sports = models.ManyToManyField(Sport)

    ## Establece la Enfermedad que presenta la Persona
    diseases = models.ManyToManyField(Disease)

    ## Establece la Discapacidad que tiene la Persona
    disabilities = models.ManyToManyField(Disability)

    ## Establece si la Persona ha leido la ley de los consejos comunales
    communal_council_law = models.BooleanField(default=False)

    ## Establece que cursos le gustaría hacer a la Persona (sin categoria de momento)
    courses = models.ManyToManyField(Course)

    ## Establece todas las organizaciones que la Persona conoce (las preguntas de arriba se redondean en esta)
    community_organizations = models.ManyToManyField(CommunityOrganization)

    ## Estable que hace la Persona en sus horas de ocio
    leisure = models.CharField(max_length=500)

    ## Estable la sugerencia que la Persona ofrece para poder mejorar la Comunicación en la Comunidad
    communication = models.CharField(max_length=500)

    ## Establece la Inseguridad que la Persona considera que hay en la comunidad
    insecurity = models.CharField(max_length=500)

    ## Establece algún comentario que la Persona quiera hacer en relación a las necesidades de la comunidad
    commentary = models.CharField(max_length=500)

    ## Establece alguna observación que se tenga sobre la persona
    observation = models.TextField()

    ## Establece la relación con el grupo familiar
    family_group = models.ForeignKey(FamilyGroup,on_delete=models.CASCADE)

    ## Cacula la edad en años que tiene una persona según su fecha de nacimiento
    def age(self):
        """!
        Método que calcula la edad de la persona

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un número entero que representa la edad
        """

        return int((datetime.date.today() - self.birthdate).days / 365.25  )

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 14-01-2018
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre, apellido y cédula de la persona
        """

        return self.first_name + ' ' + self.last_name + ', ' + str(self.identity_card)

    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')