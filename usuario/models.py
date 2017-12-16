from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import User
from base.models import ConsejoComunal

# Create your models here.

class Perfil(models.Model):

    cedula = models.CharField(
        max_length=9,
        unique=True
    )

    telefono = models.CharField(
        max_length=16,
    )

    user = models.OneToOneField(
        User, related_name="perfil",on_delete=models.CASCADE,
        help_text=_("Relación entre los datos de registro del encuestador y el usuario con acceso al sistema")
    )

    consejo_comunal = models.ForeignKey(ConsejoComunal,on_delete=models.CASCADE)

    class Meta:

        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfiles")
        ordering = ("cedula",)

    def __str__(self):

        return "%s, %s" % (self.user.first_name, self.user.last_name)
