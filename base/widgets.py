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
## @namespace base.widgets
#
# Contiene las clases, atributos y métodos para los widgets a implementar en los formularios de uso general en el sistema
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.forms import MultiWidget, Select, TextInput
from .constant import SHORT_NACIONALIDAD, TIPO_RIF, TELEFONO_CODIGO_PAIS
from django.utils.translation import ugettext_lazy as _

class RifWidget(MultiWidget):
    """!
    Clase que agrupa los widgets de los campos del tipo de rif, número de rif y dígito validador del rif

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 26-04-2016
    """

    def __init__(self, attrs=None, *args, **kwargs):

        self.attrs = attrs or {}

        widgets = (
            Select(
                attrs={
                    'class': 'select2 form-control', 'data-toggle': 'tooltip',
                    'title': _("Seleccione el tipo de R.I.F.")
                }, choices=TIPO_RIF
            ),
            TextInput(
                attrs={
                    'class': 'form-control text-center', 'placeholder': '00000000', 'data-mask': '00000000',
                    'data-toggle': 'tooltip', 'maxlength': '8', 'size': '7', 'data-rule-required': 'true',
                    'title': _("Indique el número de R.I.F., si es menor a 8 dígitos complete con ceros a la izquierda")
                }
            ),
            TextInput(
                attrs={
                    'class': 'form-control text-center', 'data-rule-required': 'true', 'data-mask': '0',
                    'title': _("Indique el último dígito del R.I.F."), 'placeholder': '0', 'maxlength': '1',
                    'size': '1', 'data-toggle': 'tooltip',
                }
            )
        )

        super(RifWidget, self).__init__(widgets, attrs, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value[0], value[1:-1], value[-1]]
        return [None, None, None]

class CedulaWidget(MultiWidget):
    """!
    Clase que agrupa los widgets de los campos de nacionalidad y número de cédula de identidad

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 26-04-2016
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
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 16-05-2016
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

class TelefonoWidget(MultiWidget):
    """!
    Clase que agrupa los widgets de los campos de un número telefónico

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 16-05-2016
    """

    def __init__(self, *args, **kwargs):

        widgets = (
            Select(
                attrs={
                    'class': 'select2 form-control', 'data-toggle': 'tooltip', 'style':'width:110px',
                    'title': _("Seleccione el código telefónico de país")
                }, choices=TELEFONO_CODIGO_PAIS
            ),
            TextInput(
                attrs={
                    'class': 'form-control input-sm', 'placeholder': '-000-0000000', 'data-mask': '-000-0000000',
                    'data-toggle': 'tooltip', 'data-rule-required': 'true', 'style': 'width:140px',
                    'title': _("Indique el número de teléfono")
                }
            )
        )

        super(TelefonoWidget, self).__init__(widgets, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value[0:4], value[4:]]
        return [None, None]
