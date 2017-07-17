from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from base.constant import SEXO, PARENTESCO, ESTADO_CIVIL, GRADO_INSTRUCCION, MISION_EDUCATIVA
from vivienda.grupo_familiar.models import GrupoFamiliar

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
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ],
    )

    telefono = models.CharField(
        max_length=18, help_text=_("Número telefónico de contacto con el usuario"),
        validators=[
            validators.RegexValidator(
                r'^\(\+\d{3}\)-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: ( ) - +")
            ),
        ]
    )

    ## Establece el correo de la persona
    correo = models.CharField(
        max_length=100, help_text=("correo@correo.com"), null=True,
    )

    ## Establece el sexo de la Persona
    sexo = models.CharField(max_length=1, choices=SEXO)

    ## Establece la fecha de nacimiento de la Persona
    fecha_nacimiento = models.DateField()

    ## Establece el parentesto que tiene el jefe familiar con el resto del Grupo Familiar
    parentesco = models.CharField(max_length=2, choices=PARENTESCO)

    ## Establece el Estado Civil de la Persona
    estado_civil = models.CharField(max_length=2, choices=ESTADO_CIVIL)

    ## Establece el Grado de Instrucción de la Persona
    grado_instruccion = models.CharField(max_length=2, choices=GRADO_INSTRUCCION)

    ## Establece la Misión Educativa que tiene la Persona
    mision_educativa = models.CharField(max_length=2, choices=MISION_EDUCATIVA)

    ## Establece la Profesión de la Persona (sin categoria de momento)
    profesion = models.CharField(max_length=100)

    ## Establece la Ocupación de la Persona (sin categoria de momento)
    ocupacion = models.CharField(max_length=100)

    ## Establece los ingresos de dinero de la Persona (sin categoria de momento)
    ingreso = models.CharField(max_length=100)

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

    ## Establece la relación con el grupo familiar
    grupo_familiar = models.ForeignKey(GrupoFamiliar)
