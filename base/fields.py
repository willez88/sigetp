"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CENDITEL (2017)

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
## @namespace base.constant
#
# Contiene las constantes de uso general en el sistema
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.forms import MultiValueField, ChoiceField, CharField, TextInput
from .constant import SHORT_NACIONALIDAD, TIPO_RIF, TELEFONO_CODIGO_PAIS
from .widgets import RifWidget, CedulaWidget, CoordenadaWidgetReadOnly, TelefonoWidget
from django.utils.translation import ugettext_lazy as _

class RifField(MultiValueField):
    """!
    Clase que agrupa los campos del tipo de rif, número de rif y dígito validador del rif en un solo campo del
    formulario

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 26-04-2016
    """
    widget = RifWidget
    default_error_messages = {
        'invalid_choices': _("Debe seleccionar un tipo de RIF válido")
    }

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': _("Debe indicar un numero de RIF"),
            'invalid': _("El valor indicado no es válido"),
            'incomplete': _("El número de RIF esta incompleto")
        }

        fields = (
            ChoiceField(choices=TIPO_RIF),
            CharField(max_length=8, min_length=8),
            CharField(max_length=1, min_length=1)
        )

        label = _("R.I.F.:")

        super(RifField, self).__init__(
            error_messages=error_messages, fields=fields, label=label, require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):

        if data_list:
            return ''.join(data_list)
        return ''

class CedulaField(MultiValueField):
    """!
    Clase que agrupa los campos de la nacionalidad y número de cédula de identidad en un solo campo del formulario

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 26-04-2016
    """
    widget = CedulaWidget
    default_error_messages = {
        'invalid_choices': _("Debe seleccionar una nacionalidad válida")
    }

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': _("Debe indicar un número de Cédula"),
            'invalid': _("El valor indicado no es válido"),
            'incomplete': _("El número de Cédula esta incompleto")
        }

        fields = (
            ChoiceField(choices=SHORT_NACIONALIDAD),
            CharField(max_length=8)
        )

        label = _("Cédula de Identidad:")

        help_text = _("Cédula de Identidad del usuario")

        super(CedulaField, self).__init__(
            error_messages=error_messages, fields=fields, label=label, help_text=help_text, require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return ''.join(data_list)
        return ''

class CoordenadaField(MultiValueField):
    """!
    Clase que agrupa los campos de coordenadas geográficas, latitud y longitud

    @author Ing. Roldan Vargas (rvargas at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 16-05-2016
    """
    widget = CoordenadaWidgetReadOnly

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': _("Debe indicar una coordenada"),
            'invalid': _("El valor indicado no es válido"),
            'incomplete': _("La coordenada esta incompleta")
        }

        fields = (
            CharField(max_length=100),
            CharField(max_length=100)
        )

        label = _("Coordenadas")

        super(CoordenadaField, self).__init__(
            error_messages=error_messages, fields=fields, label=label, require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):

        if data_list:
            return ','.join(data_list)
        return ''

class TelefonoField(MultiValueField):
    """!
    Clase que agrupa los campos de un número teléfónico

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 16-05-2016
    """

    widget = TelefonoWidget
    default_error_messages = {
        'invalid_choices': _("Debe seleccionar un codigo telefónico de país válido")
    }

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': _("Debe indicar un número de Teléfono"),
            'invalid': _("El valor indicado no es válido"),
            'incomplete': _("El número de teléfono esta incompleto")
        }

        fields = (
            ChoiceField(choices=TELEFONO_CODIGO_PAIS),
            CharField(max_length=12)
        )

        label = _("Teléfono:")

        help_text = _("Rellenar con ceros en caso de no poseer teléfono.")

        super(TelefonoField, self).__init__(
            error_messages=error_messages, fields=fields, label=label, require_all_fields=True, help_text=help_text, *args, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return ''.join(data_list)
        return ''
