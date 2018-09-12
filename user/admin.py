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
## @namespace user.admin
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
from .models import Profile, CommunalCouncilLevel, Pollster
from .forms import CommunalCouncilLevelAdminForm
from django.contrib.auth.models import User

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Perfil del usuario en el panel administrativo

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    ## Mostrar los campos
    list_display = ('user','phone',)

    ## Filtrar por campos
    list_filter = ('user__groups',)

    ## Mostrar 25 registros por página
    #list_per_page = 25

    ## Ordenar por usuario
    #ordering = ('consejo_comunal',)

    ## Buscar por campos
    #search_fields = ('telefono','user',)

## Registra el modelo Perfil en el panel administrativo
admin.site.register(Profile, ProfileAdmin)

class CommunalCouncilLevelAdmin(admin.ModelAdmin):
    form = CommunalCouncilLevelAdminForm
    change_form_template = 'user/admin/change_form.html'

    list_display = ('profile','communal_council',)
    #list_filter = ('communal_council',)
    #list_per_page = 25
    #ordering = ('communal_council',)
admin.site.register(CommunalCouncilLevel, CommunalCouncilLevelAdmin)

class PollsterAdmin(admin.ModelAdmin):
    list_display = ('profile','communal_council_level',)
    #list_filter = ('communal',)
    #list_per_page = 25
    #ordering = ('communal',)
admin.site.register(Pollster, PollsterAdmin)
