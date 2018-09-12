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
## @namespace family_group.forms
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
from .models import FamilyGroup
from base.constant import TIPO_TENENCIA
from living_place.models import LivingPlace
from user.models import CommunalCouncilLevel, Pollster
from base.models import TenureType

class FamilyGroupForm(forms.ModelForm):
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
        super(FamilyGroupForm, self).__init__(*args, **kwargs)
        living_place_list = [('','Selecione...')]
        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=user.profile)
            for li in LivingPlace.objects.filter(communal_council=communal_council_level.communal_council):
                living_place_list.append( (li.id,li) )
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            for li in LivingPlace.objects.filter(user=pollster.profile.user):
                living_place_list.append( (li.id,li) )
        self.fields['living_place'].choices = living_place_list

    ## Vivienda donde habita el grupo familiar
    living_place = forms.ChoiceField(
        label=_('Vivienda:'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Vivienda'),
            }
        )
    )

    ## Apellido del grupo familiar
    family_last_name = forms.CharField(
        label=_('Apellidos de la Familia:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique el Apellido de la Familia'),
            }
        )
    )

    ## Familia beneficiada por clap
    beneficiary_family = forms.BooleanField(
        label=_('¿La Familia ha sido beneficiada por el CLAP?'),
        required = False,
    )

    ## Tenencia que el grupo familiar tiene sobre la vivienda
    tenure = forms.ModelChoiceField(
        label=_('Tipo de Tenencia de la Vivienda:'), queryset=TenureType.objects.all(),
        empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _("Seleccione el Tipo de Tenencia de la Vivienda"), 'onchange': '__tenure(this.value)',
            }
        )
    )

    ## Alquiler de la vivienda en meses
    rented = forms.CharField(
        label=_('Tiempo Alquilado (en meses):'), widget=forms.NumberInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip',
            'title': _('Indique el tiempo que tiene como alquilado'), 'min':'0', 'step':'1', 'value':'0',
        }), required=False
    )

    ## Consulta sobre el pasaje
    ticket = forms.BooleanField(
        label=_('¿Cree Ud. que se deba consultar a las comunidades para los precios del pasaje?'),
        required = False,
    )

    ## Observación
    observation = forms.CharField(
        label=_('Observación:'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique alguna observación que pueda tener el grupo familiar'),
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

        model = FamilyGroup
        exclude = [
            'living_place'
        ]
