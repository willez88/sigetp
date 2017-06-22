"""
Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP)

Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @namespace base.widgets
#
# Contiene las clases, atributos y métodos para los widgets a implementar en los formularios
# @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>

from django.forms import MultiWidget, Select, TextInput
from .constant import SHORT_NACIONALIDAD
from django.utils.translation import ugettext_lazy as _

class CedulaWidget(MultiWidget):
    """!
    Clase que agrupa los widgets de los campos de nacionalidad y número de cédula de identidad

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 26-04-2016
    @version 1.0.0
    """

    def __init__(self, *args, **kwargs):

        widgets = (
            Select(
                attrs={
                    'class': 'select2 form-control', 'data-toggle': 'tooltip',
                    'title': _("Seleccione la nacionalidad")
                }, choices=SHORT_NACIONALIDAD
            ),
            TextInput(
                attrs={
                    'class': 'form-control text-center input-sm', 'placeholder': '00000000', 'data-mask': '00000000',
                    'data-toggle': 'tooltip', 'maxlength': '8', 'size':'7', 'data-rule-required': 'true',
                    'title': _("Indique el número de Cédula de Identidad")
                }
            )
        )

        super(CedulaWidget, self).__init__(widgets, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value[0], value[1:]]
        return [None, None]

class CoordenadaWidgetReadOnly(MultiWidget):
    """!
    Clase que agrupa los widgets de los campos para las coordenadas geográficas, latitud y longitud

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>
    @date 16-05-2016
    @version 1.0.0
    """

    def __init__(self, attrs=None, *args, **kwargs):

        self.attrs = attrs or {}

        widgets = (
            TextInput(
                attrs={
                    'class': 'form-control', 'data-toggle': 'tooltip', 'readonly': 'readonly',
                    'title': _("Coordenada de Longitud"), 'size': '15', 'placeholder': _("Longitud")
                }
            ),
            TextInput(
                attrs={
                    'class': 'form-control', 'data-toggle': 'tooltip', 'readonly': 'readonly',
                    'title': _("Coordenada de Latitud"), 'size': '15', 'placeholder': _("Latitud")
                }
            )
        )

        super(CoordenadaWidgetReadOnly, self).__init__(widgets, attrs, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value]
        return [None, None]

