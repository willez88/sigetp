from django import forms

from .constant import NATIONALITY, PHONE_PREFIX, RIF_TYPE
from .widgets import (
    CoordenateWidgetReadOnly, IdentityCardWidget, PhoneWidget, RifWidget,
)


class RifField(forms.MultiValueField):
    """!
    Clase que agrupa los campos del tipo de rif, número de rif y dígito
    validador del rif en un solo campo del formulario

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    widget = RifWidget
    default_error_messages = {
        'invalid_choices': 'Debe seleccionar un tipo de RIF válido'
    }

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': 'Debe indicar un numero de RIF',
            'invalid': 'El valor indicado no es válido',
            'incomplete': 'El número de RIF esta incompleto'
        }

        fields = (
            forms.ChoiceField(choices=RIF_TYPE),
            forms.CharField(max_length=8, min_length=8),
            forms.CharField(max_length=1, min_length=1)
        )

        label = 'R.I.F.:'

        help_text = 'C-00000000-0'

        super(RifField, self).__init__(
            error_messages=error_messages, fields=fields, label=label,
            help_text=help_text, require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return ''.join(data_list)
        return ''


class IdentityCardField(forms.MultiValueField):
    """!
    Clase que agrupa los campos de la nacionalidad y número de cédula de
    identidad en un solo campo del formulario

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    widget = IdentityCardWidget
    default_error_messages = {
        'invalid_choices': 'Debe seleccionar una nacionalidad válida'
    }

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': 'Debe indicar un número de Cédula',
            'invalid': 'El valor indicado no es válido',
            'incomplete': 'El número de Cédula esta incompleto'
        }

        fields = (
            forms.ChoiceField(choices=NATIONALITY),
            forms.CharField(max_length=8)
        )

        label = 'Cédula de Identidad:'

        help_text = 'V-00000000 ó E-00000000'

        super(IdentityCardField, self).__init__(
            error_messages=error_messages, fields=fields, label=label,
            help_text=help_text, require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return ''.join(data_list)
        return ''


class CoordinateField(forms.MultiValueField):
    """!
    Clase que agrupa los campos de coordenadas geográficas, latitud y longitud

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    widget = CoordenateWidgetReadOnly

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': 'Debe indicar una coordenada',
            'invalid': 'El valor indicado no es válido',
            'incomplete': 'La coordenada esta incompleta'
        }

        fields = (
            forms.CharField(max_length=100),
            forms.CharField(max_length=100)
        )

        label = 'Coordenadas:'

        super(CoordinateField, self).__init__(
            error_messages=error_messages, fields=fields, label=label,
            require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return ','.join(data_list)
        return ''


class PhoneField(forms.MultiValueField):
    """!
    Clase que agrupa los campos de un número teléfónico

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    widget = PhoneWidget
    default_error_messages = {
        'invalid_choices': 'Debe seleccionar un prefijo de teléfono de \
        país válido'
    }

    def __init__(self, *args, **kwargs):

        error_messages = {
            'required': 'Debe indicar un número de Teléfono',
            'invalid': 'El valor indicado no es válido',
            'incomplete': 'El número de teléfono esta incompleto'
        }

        fields = (
            forms.ChoiceField(choices=PHONE_PREFIX),
            forms.CharField(max_length=12)
        )

        label = 'Teléfono:'

        help_text = '+58-416-0000000'

        super(PhoneField, self).__init__(
            error_messages=error_messages, fields=fields, label=label,
            require_all_fields=True, help_text=help_text, *args, **kwargs
        )

    def compress(self, data_list):
        if data_list:
            return ''.join(data_list)
        return ''
