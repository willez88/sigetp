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
## @namespace living_place.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar en la aplicación vivienda
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import LivingPlace, Photograph
from base.models import (
    State, Municipality, Parish, CommunalCouncil, ElectricService, SanitarySituation, TrashDisposal,
    LivingPlaceType, RoofType, WallType, FloorType, CementType, Valoration, Animal, Risk
)
from base.fields import CoordinateField
from user.models import CommunalCouncilLevel, Pollster
import datetime

class LivingPlaceForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de la vivienda

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

        user = kwargs.pop('user')
        super(LivingPlaceForm, self).__init__(*args, **kwargs)
        self.fields['date_time'].initial = datetime.datetime.now()

        risk_list = []
        for ri in Risk.objects.all():
            risk_list.append( (ri.id,ri) )
        self.fields['risks'].choices = risk_list

        animal_list = []
        for an in Animal.objects.all():
            animal_list.append( (an.id,an) )
        self.fields['animals'].choices = animal_list

        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=user.profile)
            self.fields['communal_council'].initial = communal_council_level.communal_council
            self.fields['parish'].initial = communal_council_level.communal_council.parish
            self.fields['municipality'].initial = communal_council_level.communal_council.parish.municipality
            self.fields['state'].initial = communal_council_level.communal_council.parish.municipality.state
            self.fields['communal_council_rif'].initial = communal_council_level.communal_council.rif
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            self.fields['communal_council'].initial = pollster.communal_council_level.communal_council
            self.fields['parish'].initial = pollster.communal_council_level.communal_council.parish
            self.fields['municipality'].initial = pollster.communal_council_level.communal_council.parish.municipality
            self.fields['state'].initial = pollster.communal_council_level.communal_council.parish.municipality.state
            self.fields['communal_council_rif'].initial = pollster.communal_council_level.communal_council.rif

    ## Fecha y hora del registro de la vivienda
    date_time = forms.CharField(
        label=_('Fecha y hora:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'readonly':'true',
                'title': _('Indique la Fecha y Hora del registro'),
            }
        )
    )

    ## Número de identificación de la vivienda
    living_place_number = forms.CharField(
        label=_('Número de la Vivienda:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique el Número de la vivienda'),
            }
        )
    )

    ## Servicio eléctrico usado en la vivienda
    electric_service = forms.ModelChoiceField(
        label=_('Servicio Eléctrico:'), queryset=ElectricService.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Servicio Electrico'),
            }
        )
    )

    ## Situación sanitaria presentada en la vivienda
    sanitary_situation = forms.ModelChoiceField(
        label=_('Situación Sanitaria:'), queryset=SanitarySituation.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Situación Sanitaria'),
            }
        )
    )

    ## Disposicíon de la basura usada en la vivienda
    trash_disposal = forms.ModelChoiceField(
        label=_('Disposición de la Basura:'), queryset=TrashDisposal.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Disposición de la Basura'),
            }
        )
    )

    ## Tipo de vivienda
    living_place_type = forms.ModelChoiceField(
        label=_('Tipo de la Vivienda:'), queryset=LivingPlaceType.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Tipo de la Vivienda'),
            }
        )
    )

    ## Tipo de techo de la vivienda
    roof_type = forms.ModelChoiceField(
        label=_('Tipo del Techo:'), queryset=RoofType.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Tipo del Techo'),
            }
        )
    )

    ## Tipo de pared de la vivienda
    wall_type = forms.ModelChoiceField(
        label=_('Tipo de la Pared:'), queryset=WallType.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Tipo de la Pared'), 'onchange': 'frieze(this.value)',
            }
        )
    )

    ## Pared frizada
    wall_frieze = forms.BooleanField(
        label=_('¿La Pared está Frizada?'),
        required = False
    )

    ## Tipo del piso de la vivienda
    floor_type = forms.ModelChoiceField(
        label=_('Tipo del Piso:'), queryset=FloorType.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Tipo del Piso'), 'onchange': 'cement(this.value)',
            }
        )
    )

    ## Tipo de cemento del piso de la vivienda
    cement_type = forms.ModelChoiceField(
        label=_('Tipo del Cemento:'), queryset=CementType.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Tipo del Cemento'),
            }
        ), required = False
    )

    ## Condición presentada en la vivienda
    living_place_condition = forms.ModelChoiceField(
        label=_('Condición de la Vivienda:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Condición de la Vivienda'),
            }
        )
    )

    ## Condición del techo de la vivienda
    roof_condition = forms.ModelChoiceField(
        label=_('Condición del Techo:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Condición del Techo'),
            }
        )
    )

    ## Condición de la pared
    wall_condition = forms.ModelChoiceField(
        label=_('Condición de la Pared:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Condición de la Pared'),
            }
        )
    )

    ## Condición del piso
    floor_condition = forms.ModelChoiceField(
        label=_('Condición del Piso:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Condición del Piso'),
            }
        )
    )

    ## Condición de la ventilación
    ventilation_condition = forms.ModelChoiceField(
        label=_('Condición de la Ventilación:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Condición de la Ventilación'),
            }
        )
    )

    ## Condición de la iluminación
    ilumination_condition = forms.ModelChoiceField(
        label=_('Condición de la iluminación:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Condición de la Iluminación'),
            }
        )
    )

    ## Accesibilidad al ambulatorio
    ambulatory_accessibility = forms.ModelChoiceField(
        label=_('Accesibilidad al Ambulatorio:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Accecibilidad al Ambulatorio'),
            }
        )
    )

    ## Accesibilidad a la escuela
    school_accessibility = forms.ModelChoiceField(
        label=_('Accesibilidad a la Escuela:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Accecibilidad a la Escuela'),
            }
        )
    )

    ## Accesibilidad al liceo
    lyceum_accessibility = forms.ModelChoiceField(
        label=_('Accesibilidad al Liceo:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Accecibilidad al Liceo'),
            }
        )
    )

    ## Accesibilidad al centro de abastecimiento
    supply_center_accessibility = forms.ModelChoiceField(
        label=_('Accesibilidad al Centro de Abastecimiento:'), queryset=Valoration.objects.all(),
        empty_label = _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Accecibilidad al Centro de Abastecimiento'),
            }
        )
    )

    ## Número de habitaciones
    rooms_number = forms.CharField(
        label=_('Número de Habitaciones:'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique el Número de Habitaciones'), 'min':'0', 'step':'1',
            }
        )
    )

    ## Número de salas
    living_rooms_number = forms.CharField(
        label=_('Número de Salas:'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique el Número de Salas'), 'min':'0', 'step':'1',
            }
        )
    )

    ## Número de baños
    bathrooms_number = forms.CharField(
        label=_('Número de Baños:'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique el Número de Baños'), 'min':'0', 'step':'1',
            }
        )
    )

    ## ¿Tiene terreno la vivienda?
    has_terrain = forms.BooleanField(
        label=_('¿Tiene Terreno?'),
        widget=forms.CheckboxInput(
            attrs={
                'onclick':"terrain($(this).is(':checked'))"
            }
        ), required = False
    )

    ## Metros cuadrados de terreno que tiene la vivienda
    square_meter = forms.CharField(
        label=_('Metros Cuadrados:'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-md','data-toggle': 'tooltip',
                'title': _('Indique la cantidad de Metros Cuadrados del Terreno'), 'min':'0', 'step':'0.01', 'value':'0',
            }
        ), required=False
    )

    ## Metros cuadrados de terreno que la vivienda tiene productivos
    productive = forms.CharField(
        label=_('Productivo:'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-md','data-toggle': 'tooltip',
                'title': _('Indique la cantidad de Metros Cuadrados que están Productivos'), 'min':'0', 'step':'0.01', 'value':'0',
            }
        ), required=False
    )

    ## Metros cuadrados de terreno que la vivienda tiene sin producir
    non_productive = forms.CharField(
        label=_('Por Producir:'),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-md','data-toggle': 'tooltip',
                'title': _('Indique la cantidad de Metros Cuadrados que faltan por Producir'), 'min':'0', 'step':'0.01', 'value':'0',
            }
        ), required=False
    )

    ## Riesgo por río
    """river_risk = forms.BooleanField(
        label=_('¿Riesgo por Ríos?'),
        required = False
    )

    ## Riesgo por quebrada
    gully_risk = forms.BooleanField(
        label=_('¿Riesgo por Quebradas?'),
        required = False
    )

    ## riesgo por derrumbe
    landslides_risk = forms.BooleanField(
        label=_('¿Riesgo por Derrumbes?'),
        required = False
    )

    ## Riesgo por zona sísmica
    seismic_zone_risk = forms.BooleanField(
        label=_('¿Riesgo por Zona Sísmica?'),
        required = False
    )"""

    ## Riesgos que presenta la vivienda
    risks = forms.MultipleChoiceField(
        label = ('Riesgos que presenta la vivienda:'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2-multiple','data-toggle': 'tooltip',
                'multiple':'multiple', 'style': 'width:100%',
                'title': _('Indique los riesgo que presenta la vivienda.'),
            }
        ),
        required=False
    )

    ## Animales que hay en la vivienda
    animals = forms.MultipleChoiceField(
        label = ('Animales que tiene:'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2-multiple','data-toggle': 'tooltip',
                'multiple':'multiple', 'style': 'width:100%',
                'title': _('Indique los animales que tiene'),
            }
        ),
        required=False
    )

    ## Estado donde se encuentra ubicada la vivienda
    state = forms.CharField(
        label=_('Estado:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Muestra el estado'),
                'readonly' : 'true',
            }
        ), required=False
    )

    ## Municipio donde se encuentra ubicada la vivienda
    municipality = forms.CharField(
        label=_('Municipio:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Muestra el municipio'),
                'readonly' : 'true',
            }
        ), required=False
    )

    ## Parroquia donde se encuentra ubicada la vivienda
    parish = forms.CharField(
        label=_('Parroquia:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm','data-toggle': 'tooltip',
                'title': _('Muestra la parroquia'),
                'readonly' : 'true',
            }
        ), required=False
    )

    ## Consejo comunal donde se encuentra ubicada la vivienda
    communal_council = forms.CharField(
        label=_('Consejo Comunal:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm','data-toggle': 'tooltip',
                'title': _('Muestra el consejo comunal'),
                'readonly':'true',
            }
        ), required=False
    )

    ## Rif del consejo comunal
    communal_council_rif = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm','data-toggle': 'tooltip',
                'readonly':'true',
                'title': _('Muestra el RIF del Consejo Comunal'),
            }
        ), required=False
    )

    ## Dirección exacta de la vivienda
    address = forms.CharField(
        label=_('Dirección:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique la Dirección de la vivienda'),
            }
        )
    )

    ## Coordenadas geográficas de la vivienda
    coordinate = CoordinateField()

    ## Alguna observación acerca de la vivienda
    observation = forms.CharField(
        label=_('Observación:'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique alguna observación que pueda tener la vivienda'),
            }
        ), required = False
    )

    def clean(self):
        """!
        Método que permite validar el formulario incluyendo varios campos

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Formulario con los rectpectivos errores
        """

        cleaned_data = super(LivingPlaceForm, self).clean()
        square_meter = float(self.cleaned_data['square_meter'])
        productive = float(self.cleaned_data['productive'])
        non_productive = float(self.cleaned_data['non_productive'])

        floor_type = self.cleaned_data['floor_type']
        cement_type = self.cleaned_data['cement_type']

        if square_meter < 0:
            msg = str(_('El valor de los metros cuadrados del terreno debe ser mayor a 0'))
            self.add_error('square_meter', msg)

        if square_meter != (productive + non_productive):
            msg = str(_('El terreno productivo y por producir debe ser igual al total de metros cuadrados'))
            self.add_error('square_meter', msg)
            self.add_error('productive', msg)
            self.add_error('non_productive', msg)

        if floor_type == 'CE':
            if floor_type == '':
                msg = str(_('Este campo es obligatorio.'))
                self.add_error('cement_type', msg)

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = LivingPlace
        exclude = ['user','communal_council']

class LivingPlaceUpdateForm(LivingPlaceForm):
    """!
    Clase que contiene los campos del formulario para actualizar los datos de la vivienda

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

        super(LivingPlaceUpdateForm, self).__init__(*args, **kwargs)
        self.fields['date_time'].required = False

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = LivingPlace
        exclude = [
            'user','date_time','communal_council'
        ]

class PhotographForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de las imágenes de la vivienda

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

        user = kwargs.pop('user')
        super(PhotographForm, self).__init__(*args, **kwargs)
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

    ## Viviendas
    living_place = forms.ChoiceField(
        label=_('Vivienda:'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Vivienda'),
            }
        )
    )

    ## Nombre de la Imagen
    #name = forms.CharField(
    #    label=_('Nombre:'),
    #    widget=forms.TextInput(
    #        attrs={
    #            'class': 'form-control input-sm', 'data-toggle': 'tooltip',
    #            'title': _('Indique el nombre de la imagen'),
    #        }
    #    )
    #)

    ## Imagen de la vivienda
    picture = forms.ImageField()

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = Photograph
        exclude = [
            'living_place'
        ]
