"""
Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP)

Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @namespace base.admin
#
# Contiene las clases, atributos y métodos básicos del sistema a implementar en el panel administrativo
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>

from django.contrib import admin
from .models import ConsejoComunal
from .forms import ConsejoComunalAdminForm

class ConsejoComunalAdmin(admin.ModelAdmin):
    form = ConsejoComunalAdminForm
    change_form_template = 'admin/change_form.html'
    list_display = ('rif','nombre','parroquia',)
    list_filter = ('rif','nombre','parroquia',)
    ordering = ('rif',)
    search_fields = ('rif','nombre','parroquia',)

    """def get_form(self, request, obj=None, **kwargs):
        ## Excluye campos del formulario en el registro o actualizacion de informacion
        self.exclude = []
        self.exclude.append('estado')
        self.exclude.append('municipio')

        return super(ConsejoComunalAdmin, self).get_form(request, obj, **kwargs)"""

## Registra el modelo ConsejoComunal en el panel administrativo
admin.site.register(ConsejoComunal, ConsejoComunalAdmin)
