from base.models import TenureType
from django.db import models
from living_place.models import LivingPlace


class FamilyGroup(models.Model):
    """!
    Clase que contiene los datos de los grupos familiares

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Apellido del grupo familiar
    family_last_name = models.CharField(max_length=100)

    # Familia beneficiada por clap
    beneficiary_family = models.BooleanField(default=False)

    # Tenencia que el grupo familiar tiene sobre la vivienda
    tenure = models.ForeignKey(TenureType, on_delete=models.CASCADE)

    # Alquiler de la vivienda en meses
    rented = models.IntegerField(default=0)

    # Consulta sobre el pasaje
    ticket = models.BooleanField(default=False)

    # Observación
    observation = models.TextField()

    # Establece la relación del grupo familiar con la vivienda
    living_place = models.ForeignKey(LivingPlace, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el apellido de la
            familia y el id del grupo familiar
        """

        return self.family_last_name + ' | ' + str(self.id)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        verbose_name = 'Grupo Familiar'
        verbose_name_plural = 'Grupos Familiares'
