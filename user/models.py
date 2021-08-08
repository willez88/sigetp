from base.models import CommunalCouncil
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """!
    Clase que contiene los datos del perfil de un usuario

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Número telefónico del usuario
    phone = models.CharField(max_length=16)

    # Establece la relación entre el perfil y el user
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ('user__username',)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre y apellido
            del usuario
        """

        return '%s %s' % (self.user.first_name, self.user.last_name)


class CommunalCouncilLevel(models.Model):
    """!
    Clase que contiene los datos de un usuario del nivel consejo comunal

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Establece la relación entre el modelo ConsejoComunal y el modelo Comunal
    communal_council = models.OneToOneField(
        CommunalCouncil, on_delete=models.CASCADE
    )

    # Establece la relación entre el modelo Perfil y el modelo Comunal
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE
    )

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre, apellido del
            usuario y el consejo comunal que administra
        """

        return '%s %s | %s' % (
            self.profile.user.first_name, self.profile.user.last_name,
            self.communal_council
        )

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Nivel Consejo Comunal'
        verbose_name_plural = 'Nivel Consejos Comunales'
        # ordering = ('communal_council__name',)


class Pollster(models.Model):
    """!
    Clase que contiene los datos del perfil de un usuario del nivel encuestador

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    communal_council_level = models.ForeignKey(
        CommunalCouncilLevel, on_delete=models.CASCADE
    )

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE
    )

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre y apellido del
            usuario
        """

        return '%s %s' % (
            self.communal_council_level.profile.user.first_name,
            self.communal_council_level.profile.user.last_name
        )

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Nivel Encuestador'
        verbose_name_plural = 'Niveles Encuestadores'
