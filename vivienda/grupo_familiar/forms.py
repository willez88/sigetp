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
## @namespace grupo_familiar.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar en la aplicación grupo_familiar
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import GrupoFamiliar
from base.constant import TIPO_TENENCIA
from vivienda.models import Vivienda
from usuario.models import Communal, Pollster

class GrupoFamiliarForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario del grupo familiar

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
        @return Retorna el formulario con una configuración inicializada de forma manual
        """

        user = kwargs.pop('user')
        super(GrupoFamiliarForm, self).__init__(*args, **kwargs)
        lista_vivienda = [('','Selecione...')]
        if Communal.objects.filter(profile=user.profile):
            communal = Communal.objects.get(profile=user.profile)
            for vi in Vivienda.objects.filter(communal_council=communal.communal_council):
                lista_vivienda.append( (vi.id,vi) )
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            for vi in Vivienda.objects.filter(user=pollster.profile.user):
                lista_vivienda.append( (vi.id,vi) )
        self.fields['vivienda'].choices = lista_vivienda

    ## Vivienda donde habita el grupo familiar
    vivienda = forms.ChoiceField(
        label=_("Vivienda:"),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Vivienda"),
            }
        )
    )

    ## Apellido del grupo familiar
    apellido_familia = forms.CharField(
        label=_("Apellidos de la Familia:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Apellido de la Familia"),
            }
        )
    )

    ## Familia beneficiada por clap
    familia_beneficiada = forms.BooleanField(
        label=_("¿La Familia ha sido beneficiada por el CLAP?"),
        required = False,
    )

    ## Tenencia que el grupo familiar tiene sobre la vivienda
    tenencia = forms.ChoiceField(
        label=_("Tipo de Tenencia de la Vivienda:"),
        choices=(('',_('Seleccione...')),)+TIPO_TENENCIA,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de Tenencia de la Vivienda"), 'onchange': '__tenencia(this.value)',
            }
        )
    )

    ## Alquiler de la vivienda en meses
    alquilada = forms.CharField(
        label=_("Tiempo Alquilado (en meses):"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique el tiempo que tiene como alquilado"), 'min':'0', 'step':'1', 'value':'0',
        }), required=False
    )

    ## Consulta sobre el pasaje
    pasaje = forms.BooleanField(
        label=_("¿Cree Ud. que se deba consultar a las comunidades para los precios del pasaje?"),
        required = False,
    )

    ## Observación
    observacion = forms.CharField(
        label=_("Observación:"),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique alguna observación que pueda tener el grupo familiar"),
            }
        ), required = False
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = GrupoFamiliar
        exclude = [
            'vivienda'
        ]
