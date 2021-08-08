import datetime

from base.fields import CoordinateField
from base.models import (
    Animal, CementType, ElectricService, FloorType, LivingPlaceType, Risk,
    RoofType, SanitarySituation, TrashDisposal, Valoration, WallType,
)
from django import forms
from user.models import CommunalCouncilLevel, Pollster

from .models import LivingPlace, Photograph


class LivingPlaceForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de la vivienda

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['date_time'].initial = datetime.datetime.now()

        risk_list = []
        for ri in Risk.objects.all():
            risk_list.append((ri.id, ri))
        self.fields['risks'].choices = risk_list

        animal_list = []
        for an in Animal.objects.all():
            animal_list.append((an.id, an))
        self.fields['animals'].choices = animal_list

        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=user.profile
            )
            self.fields[
                'communal_council'
            ].initial = communal_council_level.communal_council
            self.fields[
                'parish'
            ].initial = communal_council_level.communal_council.parish
            self.fields[
                'municipality'
            ].initial = communal_council_level.communal_council.parish.\
                municipality
            self.fields[
                'state'
            ].initial = communal_council_level.communal_council.parish.\
                municipality.state
            self.fields[
                'communal_council_rif'
            ].initial = communal_council_level.communal_council.rif
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            self.fields[
                'communal_council'
            ].initial = pollster.communal_council_level.communal_council
            self.fields[
                'parish'
            ].initial = pollster.communal_council_level.communal_council.parish
            self.fields[
                'municipality'
            ].initial = pollster.communal_council_level.communal_council.\
                parish.municipality
            self.fields[
                'state'
            ].initial = pollster.communal_council_level.communal_council.\
                parish.municipality.state
            self.fields[
                'communal_council_rif'
            ].initial = pollster.communal_council_level.communal_council.rif

    # Fecha y hora del registro de la vivienda
    date_time = forms.CharField(
        label='Fecha y hora:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'readonly': 'true',
                'title': 'Indique la Fecha y Hora del registro',
            }
        )
    )

    # Número de identificación de la vivienda
    living_place_number = forms.CharField(
        label='Número de la Vivienda:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el Número de la vivienda',
            }
        )
    )

    # Servicio eléctrico usado en la vivienda
    electric_service = forms.ModelChoiceField(
        label='Servicio Eléctrico:', queryset=ElectricService.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Servicio Electrico',
            }
        )
    )

    # Situación sanitaria presentada en la vivienda
    sanitary_situation = forms.ModelChoiceField(
        label='Situación Sanitaria:', queryset=SanitarySituation.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Situación Sanitaria',
            }
        )
    )

    # Disposicíon de la basura usada en la vivienda
    trash_disposal = forms.ModelChoiceField(
        label='Disposición de la Basura:',
        queryset=TrashDisposal.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Disposición de la Basura',
            }
        )
    )

    # Tipo de vivienda
    living_place_type = forms.ModelChoiceField(
        label='Tipo de la Vivienda:', queryset=LivingPlaceType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Tipo de la Vivienda',
            }
        )
    )

    # Tipo de techo de la vivienda
    roof_type = forms.ModelChoiceField(
        label='Tipo del Techo:', queryset=RoofType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Tipo del Techo',
            }
        )
    )

    # Tipo de pared de la vivienda
    wall_type = forms.ModelChoiceField(
        label='Tipo de la Pared:', queryset=WallType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Tipo de la Pared',
                'onchange': 'frieze(this.value)',
            }
        )
    )

    # Pared frizada
    wall_frieze = forms.BooleanField(
        label='¿La Pared está Frizada?',
        required=False
    )

    # Tipo del piso de la vivienda
    floor_type = forms.ModelChoiceField(
        label='Tipo del Piso:', queryset=FloorType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Tipo del Piso',
                'onchange': 'cement(this.value)',
            }
        )
    )

    # Tipo de cemento del piso de la vivienda
    cement_type = forms.ModelChoiceField(
        label='Tipo del Cemento:', queryset=CementType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Tipo del Cemento',
            }
        ), required=False
    )

    # Condición presentada en la vivienda
    living_place_condition = forms.ModelChoiceField(
        label='Condición de la Vivienda:', queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Condición de la Vivienda',
            }
        )
    )

    # Condición del techo de la vivienda
    roof_condition = forms.ModelChoiceField(
        label='Condición del Techo:', queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Condición del Techo',
            }
        )
    )

    # Condición de la pared
    wall_condition = forms.ModelChoiceField(
        label='Condición de la Pared:', queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Condición de la Pared',
            }
        )
    )

    # Condición del piso
    floor_condition = forms.ModelChoiceField(
        label='Condición del Piso:', queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Condición del Piso',
            }
        )
    )

    # Condición de la ventilación
    ventilation_condition = forms.ModelChoiceField(
        label='Condición de la Ventilación:',
        queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Condición de la Ventilación',
            }
        )
    )

    # Condición de la iluminación
    ilumination_condition = forms.ModelChoiceField(
        label='Condición de la iluminación:',
        queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Condición de la Iluminación',
            }
        )
    )

    # Accesibilidad al ambulatorio
    ambulatory_accessibility = forms.ModelChoiceField(
        label='Accesibilidad al Ambulatorio:',
        queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Accecibilidad al Ambulatorio',
            }
        )
    )

    # Accesibilidad a la escuela
    school_accessibility = forms.ModelChoiceField(
        label='Accesibilidad a la Escuela:', queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Accecibilidad a la Escuela',
            }
        )
    )

    # Accesibilidad al liceo
    lyceum_accessibility = forms.ModelChoiceField(
        label='Accesibilidad al Liceo:', queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Accecibilidad al Liceo',
            }
        )
    )

    # Accesibilidad al centro de abastecimiento
    supply_center_accessibility = forms.ModelChoiceField(
        label='Accesibilidad al Centro de Abastecimiento:',
        queryset=Valoration.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Accecibilidad al Centro de \
                    Abastecimiento',
            }
        )
    )

    # Número de habitaciones
    rooms_number = forms.CharField(
        label='Número de Habitaciones:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el Número de Habitaciones', 'min': '0',
                'step': '1',
            }
        )
    )

    # Número de salas
    living_rooms_number = forms.CharField(
        label='Número de Salas:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el Número de Salas', 'min': '0',
                'step': '1',
            }
        )
    )

    # Número de baños
    bathrooms_number = forms.CharField(
        label='Número de Baños:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el Número de Baños', 'min': '0', 'step': '1',
            }
        )
    )

    # ¿Tiene terreno la vivienda?
    has_terrain = forms.BooleanField(
        label='¿Tiene Terreno?',
        widget=forms.CheckboxInput(
            attrs={
                'onclick': "terrain($(this).is(':checked'))"
            }
        ), required=False
    )

    # Metros cuadrados de terreno que tiene la vivienda
    square_meter = forms.CharField(
        label='Metros Cuadrados:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-md', 'data-toggle': 'tooltip',
                'title': 'Indique la cantidad de Metros Cuadrados del Terreno',
                'min': '0', 'step': '0.01', 'value': '0',
            }
        ), required=False
    )

    # Metros cuadrados de terreno que la vivienda tiene productivos
    productive = forms.CharField(
        label='Productivo:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-md', 'data-toggle': 'tooltip',
                'title': 'Indique la cantidad de Metros Cuadrados que están \
                    Productivos',
                'min': '0', 'step': '0.01', 'value': '0',
            }
        ), required=False
    )

    # Metros cuadrados de terreno que la vivienda tiene sin producir
    non_productive = forms.CharField(
        label='Por Producir:',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-md', 'data-toggle': 'tooltip',
                'title': 'Indique la cantidad de Metros Cuadrados que faltan \
                    por Producir',
                'min': '0', 'step': '0.01', 'value': '0',
            }
        ), required=False
    )

    # Riesgos que presenta la vivienda
    risks = forms.MultipleChoiceField(
        label='Riesgos que presenta la vivienda:',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'style': 'width:100%',
                'title': 'Indique los riesgo que presenta la vivienda.',
            }
        ),
        required=False
    )

    # Animales que hay en la vivienda
    animals = forms.MultipleChoiceField(
        label='Animales que tiene:',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'style': 'width:100%',
                'title': 'Indique los animales que tiene',
            }
        ),
        required=False
    )

    # Estado donde se encuentra ubicada la vivienda
    state = forms.CharField(
        label='Estado:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Muestra el estado', 'readonly': 'true',
            }
        ), required=False
    )

    # Municipio donde se encuentra ubicada la vivienda
    municipality = forms.CharField(
        label='Municipio:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Muestra el municipio', 'readonly': 'true',
            }
        ), required=False
    )

    # Parroquia donde se encuentra ubicada la vivienda
    parish = forms.CharField(
        label='Parroquia:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Muestra la parroquia', 'readonly': 'true',
            }
        ), required=False
    )

    # Consejo comunal donde se encuentra ubicada la vivienda
    communal_council = forms.CharField(
        label='Consejo Comunal:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Muestra el consejo comunal', 'readonly': 'true',
            }
        ), required=False
    )

    # Rif del consejo comunal
    communal_council_rif = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'readonly': 'true',
                'title': 'Muestra el RIF del Consejo Comunal',
            }
        ), required=False
    )

    # Dirección exacta de la vivienda
    address = forms.CharField(
        label='Dirección:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique la Dirección de la vivienda',
            }
        )
    )

    # Coordenadas geográficas de la vivienda
    coordinate = CoordinateField()

    # Alguna observación acerca de la vivienda
    observation = forms.CharField(
        label='Observación:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique alguna observación que pueda tener la \
                    vivienda',
            }
        ), required=False
    )

    def clean(self):
        """!
        Método que permite validar el formulario incluyendo varios campos

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Formulario con los rectpectivos errores
        """

        cleaned_data = super().clean()
        square_meter = float(self.cleaned_data['square_meter'])
        productive = float(self.cleaned_data['productive'])
        non_productive = float(self.cleaned_data['non_productive'])

        floor_type = self.cleaned_data['floor_type']
        cement_type = self.cleaned_data['cement_type']

        if square_meter < 0:
            self.add_error(
                'square_meter',
                'El valor de los metros cuadrados del terreno debe ser \
                mayor a 0'
            )

        if square_meter != (productive + non_productive):
            self.add_error(
                'square_meter',
                'El terreno productivo y por producir debe ser igual al \
                    total de metros cuadrados'
            )
            self.add_error(
                'productive',
                'El terreno productivo y por producir debe ser igual al \
                    total de metros cuadrados'
            )
            self.add_error(
                'non_productive',
                'El terreno productivo y por producir debe ser igual al \
                    total de metros cuadrados'
            )

        if floor_type.id == 2:
            if floor_type == '':
                self.add_error('cement_type', 'Este campo es obligatorio.')

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        model = LivingPlace
        exclude = ['user', 'communal_council']


class LivingPlaceUpdateForm(LivingPlaceForm):
    """!
    Clase que contiene los campos del formulario para actualizar los datos de
    la vivienda

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        super().__init__(*args, **kwargs)
        self.fields['date_time'].required = False

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        model = LivingPlace
        exclude = [
            'user', 'date_time', 'communal_council'
        ]


class PhotographForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de las imágenes de la vivienda

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez <wpaez@cenditel.gob.ve>
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        living_place_list = [('', 'Selecione...')]
        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=user.profile
            )
            for li in LivingPlace.objects.filter(
                communal_council=communal_council_level.communal_council
            ):
                living_place_list.append((li.id, li))
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            for li in LivingPlace.objects.filter(user=pollster.profile.user):
                living_place_list.append((li.id, li))
        self.fields['living_place'].choices = living_place_list

    # Viviendas
    living_place = forms.ChoiceField(
        label='Vivienda:',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Vivienda',
            }
        )
    )

    # Nombre de la Imagen
    # name = forms.CharField(
    #    label=_('Nombre:'),
    #    widget=forms.TextInput(
    #        attrs={
    #            'class': 'form-control input-sm', 'data-toggle': 'tooltip',
    #            'title': _('Indique el nombre de la imagen'),
    #        }
    #    )
    # )

    # Imagen de la vivienda
    picture = forms.ImageField()

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        model = Photograph
        exclude = [
            'living_place'
        ]
