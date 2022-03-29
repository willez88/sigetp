from django import forms

from .constant import NATIONALITY, PHONE_PREFIX, RIF_TYPE


class RifWidget(forms.MultiWidget):
    """!
    Clase que agrupa los widgets de los campos del tipo de rif, número de rif y
    dígito validador del rif

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, attrs=None, *args, **kwargs):
        self.attrs = attrs or {}
        widgets = (
            forms.Select(
                attrs={
                    'class': 'select2 form-control', 'data-toggle': 'tooltip',
                    'title': 'Seleccione el tipo de R.I.F.'
                }, choices=RIF_TYPE
            ),
            forms.TextInput(
                attrs={
                    'class': 'form-control text-center',
                    'placeholder': '00000000', 'data-mask': '00000000',
                    'data-toggle': 'tooltip', 'maxlength': '8', 'size': '7',
                    'title': 'Indique el número de R.I.F., si es menor a 8 \
                        dígitos complete con ceros a la izquierda'
                }
            ),
            forms.TextInput(
                attrs={
                    'class': 'form-control text-center', 'data-mask': '0',
                    'title': 'Indique el último dígito del R.I.F.',
                    'placeholder': '0', 'maxlength': '1',
                    'size': '1', 'data-toggle': 'tooltip',
                }
            )
        )
        super().__init__(widgets, attrs, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value[0], value[1:-1], value[-1]]
        return [None, None, None]


class IdentityCardWidget(forms.MultiWidget):
    """!
    Clase que agrupa los widgets de los campos de nacionalidad y número de
    cédula de identidad

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, *args, **kwargs):
        widgets = (
            forms.Select(
                attrs={
                    'class': 'select2 form-control', 'data-toggle': 'tooltip',
                    'title': 'Seleccione la nacionalidad'
                }, choices=NATIONALITY
            ),
            forms.TextInput(
                attrs={
                    'class': 'form-control text-center input-sm',
                    'placeholder': '00000000', 'data-mask': '00000000',
                    'data-toggle': 'tooltip', 'maxlength': '8', 'size': '7',
                    'title': 'Indique el número de Cédula de Identidad'
                }
            )
        )
        super().__init__(widgets, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value[0], value[1:]]
        return [None, None]


class CoordenateWidgetReadOnly(forms.MultiWidget):
    """!
    Clase que agrupa los widgets de los campos para las coordenadas
    geográficas, latitud y longitud

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, attrs=None, *args, **kwargs):
        self.attrs = attrs or {}
        widgets = (
            forms.TextInput(
                attrs={
                    'class': 'form-control', 'data-toggle': 'tooltip',
                    'readonly': 'readonly', 'title': 'Coordenada de Longitud',
                    'size': '15', 'placeholder': 'Longitud'
                }
            ),
            forms.TextInput(
                attrs={
                    'class': 'form-control', 'data-toggle': 'tooltip',
                    'readonly': 'readonly', 'title': 'Coordenada de Latitud',
                    'size': '15', 'placeholder': 'Latitud'
                }
            )
        )
        super().__init__(widgets, attrs, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value]
        return [None, None]


class PhoneWidget(forms.MultiWidget):
    """!
    Clase que agrupa los widgets de los campos de un número telefónico

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, *args, **kwargs):
        widgets = (
            forms.Select(
                attrs={
                    'class': 'select2 form-control', 'data-toggle': 'tooltip',
                    'title': 'Seleccione el código telefónico de país'
                }, choices=PHONE_PREFIX
            ),
            forms.TextInput(
                attrs={
                    'class': 'form-control input-sm',
                    'placeholder': '-000-0000000', 'data-mask': '-000-0000000',
                    'data-toggle': 'tooltip',
                    'title': 'Indique el número de teléfono'
                }
            )
        )
        super().__init__(widgets, *args, **kwargs)

    def format_output(self, rendered_widgets):
        return ' - '.join(rendered_widgets)

    def decompress(self, value):
        if value:
            return [value[0:4], value[4:]]
        return [None, None]
