from base.models import (
    Animal, CementType, CommunalCouncil, ElectricService, FloorType,
    LivingPlaceType, Risk, RoofType, SanitarySituation, TrashDisposal,
    Valoration, WallType,
)
from django.contrib.auth.models import User
from django.db import models


class LivingPlace(models.Model):
    """!
    Clase que contiene los datos de la vivienda

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Fecha y hora del registro de la vivienda
    date_time = models.DateTimeField()

    # Servicio eléctrico
    electric_service = models.ForeignKey(
        ElectricService, on_delete=models.CASCADE
    )

    # Situación sanitaria
    sanitary_situation = models.ForeignKey(
        SanitarySituation, on_delete=models.CASCADE
    )

    # Disposición de la basura
    trash_disposal = models.ForeignKey(
        TrashDisposal, on_delete=models.CASCADE
    )

    # Tipo de la vivienda
    living_place_type = models.ForeignKey(
        LivingPlaceType, on_delete=models.CASCADE
    )

    # Tipo del techo
    roof_type = models.ForeignKey(RoofType, on_delete=models.CASCADE)

    # Tipo de la pared
    wall_type = models.ForeignKey(WallType, on_delete=models.CASCADE)

    # La pared está frizada o no
    wall_frieze = models.BooleanField(default=False)

    # Tipo del piso
    floor_type = models.ForeignKey(FloorType, on_delete=models.CASCADE)

    # Tipo del cemento del piso
    cement_type = models.ForeignKey(
        CementType, on_delete=models.CASCADE, null=True
    )

    # Condición de la vivienda
    living_place_condition = models.ForeignKey(
        Valoration, on_delete=models.CASCADE
    )

    # COndición del techo
    roof_condition = models.ForeignKey(
        Valoration, on_delete=models.CASCADE,
        related_name='roof_condition'
    )

    # Condición de la pared
    wall_condition = models.ForeignKey(
        Valoration, on_delete=models.CASCADE, related_name='wall_condition'
    )

    # Condición del piso
    floor_condition = models.ForeignKey(
        Valoration, on_delete=models.CASCADE, related_name='floor_condition'
    )

    # Condición de la ventilación
    ventilation_condition = models.ForeignKey(
        Valoration, on_delete=models.CASCADE,
        related_name='ventilation_condition'
    )

    # Condición de la iluminación
    ilumination_condition = models.ForeignKey(
        Valoration, on_delete=models.CASCADE,
        related_name='ilumination_condition'
    )

    # Accesibilidad al ambulatorio
    ambulatory_accessibility = models.ForeignKey(
        Valoration, on_delete=models.CASCADE, related_name='ambulatory'
    )

    # Accesibilidad a la escuela
    school_accessibility = models.ForeignKey(
        Valoration, on_delete=models.CASCADE, related_name='school'
    )

    # Accesibilidad al liceo
    lyceum_accessibility = models.ForeignKey(
        Valoration, on_delete=models.CASCADE, related_name='lyceum'
    )

    # Accesibilidad al centro de abastecimiento
    supply_center_accessibility = models.ForeignKey(
        Valoration, on_delete=models.CASCADE, related_name='supply_center'
    )

    # Número de habitaciones
    rooms_number = models.IntegerField()

    # Número de salas
    living_rooms_number = models.IntegerField()

    # Número de baños
    bathrooms_number = models.IntegerField()

    # ¿Tiene terreno?
    has_terrain = models.BooleanField()

    # Metros cuadrados del terreno
    square_meter = models.DecimalField(
        max_digits=18, decimal_places=2, default=0.0
    )

    # Terreno que está productivo
    productive = models.DecimalField(
        max_digits=18, decimal_places=2, default=0.0
    )

    # Terreno que está por producir
    non_productive = models.DecimalField(
        max_digits=18, decimal_places=2, default=0.0
    )

    # Riesgo que presenta la vivienda
    risks = models.ManyToManyField(Risk)

    # Animales que hay en la vivienda
    animals = models.ManyToManyField(Animal)

    # Número de identificación de la vivienda
    living_place_number = models.CharField(max_length=20)

    # Dirección exacta de la vivienda
    address = models.CharField(max_length=500)

    # Coordenadas geográficas
    coordinate = models.CharField(max_length=255, blank=True)

    # Observación
    observation = models.TextField()

    # Establece la relación de la vivienda con el consejo comunal
    communal_council = models.ForeignKey(
        CommunalCouncil, on_delete=models.CASCADE
    )

    # Establece la relación de la vivienda con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el número de
            identificación y el id de la vivienda
        """

        return self.living_place_number + ' | ' + str(self.id)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        verbose_name = 'Vivienda'
        verbose_name_plural = 'Viviendas'
        # ordering = ('user__username',)


class Photograph(models.Model):
    """!
    Clase que contiene los datos de imágenes de la vivienda

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Nombre de la imagen
    # name = models.CharField(max_length=100)

    # Nombre de la imagen
    picture = models.ImageField(upload_to='living_place/')

    # Establece la relación de las imágenes con la vivienda
    living_place = models.ForeignKey(LivingPlace, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Una cadena de caracteres con el nombre de la imagen
        """

        return str(self.picture)

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        verbose_name = 'Fotografía'
        verbose_name_plural = 'Fotografías'
