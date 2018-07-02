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
## @namespace base.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar de manera genera en el sistema
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import State, Municipality, Parish, CommunalCouncil
from .fields import RifField

class CommunalCouncilAdminForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario del consejo comunal

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        super(CommunalCouncilAdminForm, self).__init__(*args, **kwargs)
        # Si se ha seleccionado un estado establece el listado de municipios y elimina el atributo disable
        if 'state' in self.data and self.data['state']:
            self.fields['municipality'].widget.attrs.pop('disabled')
            self.fields['municipality'].queryset=Municipality.objects.filter(state=self.data['state'])

            # Si se ha seleccionado un municipio establece el listado de parroquias y elimina el atributo disable
            if 'municipality' in self.data and self.data['municipality']:
                self.fields['parish'].widget.attrs.pop('disabled')
                self.fields['parish'].queryset=Parish.objects.filter(municipality=self.data['municipality'])

    ## Rif del consejo comunal
    rif = RifField()

    ## Nombre del consejo comunal
    name = forms.CharField(
        label=_("Nombre del Consejo Comunal:"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique el Nombre del RIF"),
            }
        )
    )

    ## Estado donde se ecnuetra ubicado el municipio
    state = forms.ModelChoiceField(
        label=_("Estado:"), queryset=State.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': _("Seleccione el estado en donde se encuentra ubicada"),
        })
    )

    ## Municipio donde se encuentra ubicada la parroquia
    municipality = forms.ModelChoiceField(
        label=_("Municipio:"), queryset=Municipality.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _("Seleccione el municipio en donde se encuentra ubicada"),
        })
    )

    ## Parroquia donde se encuentra ubicado el consejo comunal
    parish = forms.ModelChoiceField(
        label=_("Parroquia:"), queryset=Parish.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _("Seleccione la parroquia en donde se encuentra ubicada"),
        })
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 25-05-2017
        """

        model = CommunalCouncil
        fields = [
            'rif','name','state','municipality','parish'
        ]
