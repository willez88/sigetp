from django.core import validators
from django.db import models


class Country(models.Model):
    """!
    Clase que contiene los paises

    @author Ing. Roldan Vargas <rvargas@cenditel.gob.ve>
    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre del país
    name = models.CharField(max_length=80)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del país
        """

        return self.name


class State(models.Model):
    """!
    Clase que contiene los estados

    @author Ing. Roldan Vargas <rvargas@cenditel.gob.ve>
    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre del Estado
    name = models.CharField(max_length=50)

    # Establece la relación del estado con el país
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del estado
        """

        return self.name


class Municipality(models.Model):
    """!
    Clase que contiene los municipios

    @author Ing. Roldan Vargas <rvargas@cenditel.gob.ve>
    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre del Municipio
    name = models.CharField(max_length=50)

    # Establece la relación del municipio con el estado
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del municipio
        """

        return self.name


class City(models.Model):
    """!
    Clase que contiene las ciudades

    @author Ing. Roldan Vargas <rvargas@cenditel.gob.ve>
    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre de la Ciudad
    name = models.CharField(max_length=50)

    # Establece la relación de la ciudad con el estado
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la ciudad
        """

        return self.name


class Parish(models.Model):
    """!
    Clase que contiene las parroquias

    @author Ing. Roldan Vargas <rvargas@cenditel.gob.ve>
    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre de la Parroquia
    name = models.CharField(max_length=50)

    # Establece la relación de la parroquia con el municipio
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la parroquia
        """

        return self.name


class CommunalCouncil(models.Model):
    """!
    Clase que contiene los consejos comunales

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Número de rif del consejo comunal
    rif = models.CharField(
        max_length=10, help_text='Rif del Consejo Comunal',
        validators=[
            validators.RegexValidator(
                r'^C[\d]{9}$',
                'Introduzca un rif válido. Solo se permite la letra C y 9 \
                números.'
            ),
        ],
        unique=True
    )

    # Nombre del Consejo Comunal
    name = models.CharField(max_length=500)

    # Establece la relación del consejo comunal con la parroquia
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del consejo
            comunal
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Consejo Comunal'
        verbose_name_plural = 'Consejos Comunales'


class LivingPlaceType(models.Model):
    """!
    Clase que contiene los tipos de vivienda

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del tipo de
            vivienda
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Tipo de Vivienda'
        verbose_name_plural = 'Tipos de Vivienda'
        ordering = ('name',)


class RoofType(models.Model):
    """!
    Clase que contiene los tipos de techo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del tipo de
            techo
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Tipo de Techo'
        verbose_name_plural = 'Tipos de Techo'
        ordering = ('name',)


class WallType(models.Model):
    """!
    Clase que contiene los tipos de pared

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del tipo de
            pared
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Tipo de Pared'
        verbose_name_plural = 'Tipos de Pared'
        ordering = ('name',)


class FloorType(models.Model):
    """!
    Clase que contiene los tipos de piso

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del tipo de
            piso
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Tipo de Piso'
        verbose_name_plural = 'Tipos de Piso'
        ordering = ('name',)


class ElectricService(models.Model):
    """!
    Clase que contiene datos del Servicio eléctrico

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del servicio
            eléctrico
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Servicio Eléctrico'
        verbose_name_plural = 'Servicios Eléctricos'
        ordering = ('name',)


class SanitarySituation(models.Model):
    """!
    Clase que contiene datos de la situación sanitaria

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la situación
            sanitaria
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Situación Sanitaria'
        verbose_name_plural = 'Situaciones Sanitarias'
        ordering = ('name',)


class TrashDisposal(models.Model):
    """!
    Clase que contiene datos de la disposición de la basura

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la
            disposición de la basura
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Disposición de la Basura'
        verbose_name_plural = 'Disposiciones de la Basura'
        ordering = ('name',)


class TenureType(models.Model):
    """!
    Clase que contiene datos del tipo de tenencia

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del tipo de
            tenencia
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Tipo de tenencia'
        verbose_name_plural = 'Tipos de tenencia'
        ordering = ('name',)


class Relationship(models.Model):
    """!
    Clase que contiene datos del parentesco

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del parentesco
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Parentesco'
        verbose_name_plural = 'Parentescos'
        ordering = ('name',)


class MaritalStatus(models.Model):
    """!
    Clase que contiene datos del estado civil

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=30)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del estado
            civil
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estados Civiles'
        ordering = ('name',)


class InstructionDegree(models.Model):
    """!
    Clase que contiene datos del grado de instrucción

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=50)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del grado de
            instrucción
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Grado de Instrucción'
        verbose_name_plural = 'Grados de Instrucción'
        ordering = ('name',)


class EducationalMission(models.Model):
    """!
    Clase que contiene datos de la misión educativa

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=50)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la misión
            educación
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Misión Educativa'
        verbose_name_plural = 'Misiones Educativas'
        ordering = ('name',)


class SocialMission(models.Model):
    """!
    Clase que contiene datos de la misión social

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=50)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la misión
            social
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Misión Social'
        verbose_name_plural = 'Misiones Sociales'
        ordering = ('name',)


class IncomeType(models.Model):
    """!
    Clase que contiene datos del tipo de ingreso

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=50)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del tipo de
            ingreso
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Tipo de Ingreso'
        verbose_name_plural = 'Tipos de Ingreso'
        ordering = ('name',)


class CommunityOrganization(models.Model):
    """!
    Clase que contiene datos de la organización comunitaria

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=100)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la
            organización comunitaria
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Organización Comunitaria'
        verbose_name_plural = 'Organizaciones Comunitarias'
        ordering = ('name',)


class Gender(models.Model):
    """!
    Clase que contiene datos del género

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del género
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ('name',)


class CementType(models.Model):
    """!
    Clase que contiene datos del tipo de cemento

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del tipo de
            cemento
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Tipo de Cemento'
        verbose_name_plural = 'Tipos de Cemento'
        ordering = ('name',)


class Valoration(models.Model):
    """!
    Clase que contiene datos de la valoración

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la
            valoración
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Valoración'
        verbose_name_plural = 'Valoraciones'
        ordering = ('name',)


class Animal(models.Model):
    """!
    Clase que contiene datos de animales

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=20)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del animal
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'
        ordering = ('name',)


class Profession(models.Model):
    """!
    Clase que contiene datos de profesión

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=100)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la profesión
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Profesión'
        verbose_name_plural = 'Profesiones'
        ordering = ('name',)


class Occupation(models.Model):
    """!
    Clase que contiene datos de la ocupación

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=100)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la ocupación
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Ocupación'
        verbose_name_plural = 'Ocupaciones'
        ordering = ('name',)


class Workplace(models.Model):
    """!
    Clase que contiene datos del lugar de trabajo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=100)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del lugar de
            trabajo
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Lugar de Trabajo'
        verbose_name_plural = 'Lugares de Trabajo'
        ordering = ('name',)


class Sport(models.Model):
    """!
    Clase que contiene datos de deportes

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=100)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del deporte
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Deporte'
        verbose_name_plural = 'Deportes'
        ordering = ('name',)


class Disease(models.Model):
    """!
    Clase que contiene datos de enfermedades

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=150)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la
            enfermedad
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Enfermedad'
        verbose_name_plural = 'Enfermedades'
        ordering = ('name',)


class Disability(models.Model):
    """!
    Clase que contiene datos de discapacidades

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=150)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre de la
            discapacidad
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Discapacidad'
        verbose_name_plural = 'Discapacidades'
        ordering = ('name',)


class Course(models.Model):
    """!
    Clase que contiene datos de los cursos

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=100)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del curso
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('name',)


class Risk(models.Model):
    """!
    Clase que contiene datos de los cursos

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Nombre
    name = models.CharField(max_length=100)

    def __str__(self):
        """!
        Método para representar la clase de forma amigable

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Devuelve una cadena de caracteres con el nombre del riesgo
        """

        return self.name

    class Meta:
        """!
        Meta clase del modelo que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        verbose_name = 'Riesgo'
        verbose_name_plural = 'Riesgos'
        ordering = ('name',)
