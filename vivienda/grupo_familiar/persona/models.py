from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from base.constant import SEXO, PARENTESCO, ESTADO_CIVIL, GRADO_INSTRUCCION, MISION_EDUCATIVA, TIPO_INGRESO, MISION_SOCIAL
from vivienda.grupo_familiar.models import GrupoFamiliar
import datetime

# Create your models here.

class Persona(models.Model):

    ## Nombre de la Persona
    nombre = models.CharField(max_length=100)

    ## Apellido de la Persona
    apellido = models.CharField(max_length=100)

    ## Cédula de la Persona. Si tiene o no
    cedula = models.CharField(
        max_length=9,
        help_text=_("Cédula de Identidad del usuario"),
        unique=True,
        null=True
    )

    # +058-416-0708340
    telefono = models.CharField(
        max_length=16,
        help_text=_("Número telefónico de contacto con el usuario"),
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
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25  )
