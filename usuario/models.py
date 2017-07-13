from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):

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
        max_length=18, help_text=_("Número telefónico de contacto con el usuario"),
        validators=[
            validators.RegexValidator(
                r'^\(\+\d{3}\)-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: ( ) - +")
            ),
        ]
    )

    user = models.OneToOneField(
        User, related_name="perfil",
        help_text=_("Relación entre los datos de registro del encuestador y el usuario con acceso al sistema")
    )

    class Meta:

        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfiles")
        ordering = ("cedula",)

    def __str__(self):

        return "%s, %s" % (self.user.first_name, self.user.last_name)
