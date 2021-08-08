from base.models import TenureType
from django import forms
from living_place.models import LivingPlace
from user.models import CommunalCouncilLevel, Pollster

from .models import FamilyGroup


class FamilyGroupForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario del grupo familiar

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
        @return Retorna el formulario con una configuración inicializada de
            forma manual
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

    # Vivienda donde habita el grupo familiar
    living_place = forms.ChoiceField(
        label='Vivienda:',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Vivienda',
            }
        )
    )

    # Apellido del grupo familiar
    family_last_name = forms.CharField(
        label='Apellidos de la Familia:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el Apellido de la Familia',
            }
        )
    )

    # Familia beneficiada por clap
    beneficiary_family = forms.BooleanField(
        label='¿La Familia ha sido beneficiada por el CLAP?',
        required=False,
    )

    # Tenencia que el grupo familiar tiene sobre la vivienda
    tenure = forms.ModelChoiceField(
        label='Tipo de Tenencia de la Vivienda:',
        queryset=TenureType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Tipo de Tenencia de la Vivienda',
                'onchange': '__tenure(this.value)',
            }
        )
    )

    # Alquiler de la vivienda en meses
    rented = forms.CharField(
        label='Tiempo Alquilado (en meses):',
        widget=forms.NumberInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip',
            'title': 'Indique el tiempo que tiene como alquilado', 'min': '0',
            'step': '1', 'value': '0',
        }), required=False
    )

    # Consulta sobre el pasaje
    ticket = forms.BooleanField(
        label='¿Cree Ud. que se deba consultar a las comunidades para los \
            precios del pasaje?',
        required=False,
    )

    # Observación
    observation = forms.CharField(
        label='Observación:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique alguna observación que pueda tener el \
                    grupo familiar',
            }
        ), required=False
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        model = FamilyGroup
        exclude = [
            'living_place'
        ]
