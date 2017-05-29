from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
# Create your models here.

class Encuestador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(
        max_length=9, help_text=_("Cédula de Identidad del usuario"),
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ]
    )
    telefono = models.CharField(
        max_length=20, help_text=_("Número telefónico de contacto con el usuario"),
        validators=[
            validators.RegexValidator(
                r'^\(\d{3}\)-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números, y los signos + o -")
            ),
        ]
    )
    correo = models.CharField(
        max_length=100, help_text=("correo@correo.com")
    )
