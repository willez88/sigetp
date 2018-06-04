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
## @namespace usuario.admin
#
# Contiene las clases, atributos y métodos básicos del sistema a implementar en el panel administrativo
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .forms import PerfilAdminForm
from .models import Perfil
from django.contrib.auth.models import User

# Register your models here.

# Se quita del registro User
#admin.site.unregister(User)

"""class PerfilInline(admin.StackedInline):
    ""
    Clase que agrega modelo Perfil en el panel administrativo y lo muestra en línea

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    ""

    model = Perfil
    form = PerfilAdminForm
    change_form_template = 'admin/change_form.html'

class PerfilAdmin(UserAdmin):
    ""
    Clase que agrega modelo Perfil junto con el modelo User en el panel administrativo

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    ""

    inlines = (PerfilInline,)

admin.site.register(User, PerfilAdmin)"""

class PerfilAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Perfil del usuario en el panel administrativo

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    form = PerfilAdminForm
    change_form_template = 'change_form.html'

    ## Mostrar los campos
    list_display = ('user','cedula','telefono','consejo_comunal',)

    ## Filtrar por campos
    list_filter = ('consejo_comunal',)

    ## Mostrar 25 registros por página
    list_per_page = 25

    ## Ordenar por usuario
    ordering = ('consejo_comunal',)

    ## Buscar por campos
    #search_fields = ('telefono','user',)

## Registra el modelo Perfil en el panel administrativo
admin.site.register(Perfil, PerfilAdmin)
