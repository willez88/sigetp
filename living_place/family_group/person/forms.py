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
## @namespace person.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar en la aplicación persona
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Person
from living_place.family_group.models import FamilyGroup
from base.fields import IdentityCardField, PhoneField
from base.models import (
    Sex, FamilyRelationship, MaritalStatus, InstructionDegree, EducationalMission, SocialMission,
    Profession, Occupation, IncomeType, Sport, Disease, Disability, Course, CommunityOrganization,
    Workplace
)
from django.core import validators
from user.models import CommunalCouncilLevel, Pollster

class PersonForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de persona

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
        super(PersonForm, self).__init__(*args, **kwargs)
        family_group_list = [('','Selecione...')]
        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=user.profile)
            for fg in FamilyGroup.objects.filter(living_place__communal_council=communal_council_level.communal_council):
                family_group_list.append( (fg.id,fg) )
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            for fg in FamilyGroup.objects.filter(living_place__user=pollster.profile.user):
                family_group_list.append( (fg.id,fg) )
        self.fields['family_group'].choices = family_group_list

        sports_list = []
        for sp in Sport.objects.all():
            sports_list.append( (sp.id,sp) )
        self.fields['sports'].choices = sports_list

        diseases_list = []
        for di in Disease.objects.all():
            diseases_list.append( (di.id,di) )
        self.fields['diseases'].choices = diseases_list

        disabilities_list = []
        for dis in Disability.objects.all():
            disabilities_list.append( (dis.id,dis) )
        self.fields['disabilities'].choices = disabilities_list

        courses_list = []
        for co in Course.objects.all():
            courses_list.append( (co.id,co) )
        self.fields['courses'].choices = courses_list

        community_organizations_list = []
        for com in CommunityOrganization.objects.all():
            community_organizations_list.append( (com.id,com) )
        self.fields['community_organizations'].choices = community_organizations_list

    ## Grupo familiar al que la persona pertenece
    family_group = forms.ChoiceField(
        label=_('Grupo Familiar:'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione El Grupo Familiar al cual pertenece la Persona'),
            }
        )
    )

    ## Nonbres
    first_name = forms.CharField(
        label=_('Nombres:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Nombres de la Persona'),
            }
        )
    )

    ## Apellidos
    last_name = forms.CharField(
        label=_('Apellidos:'),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique los Apellidos de la Persona'),
            }
        )
    )

    ## ¿Tiene cédula?
    has_identity_card = forms.ChoiceField(
        label=_('¿Tiene Cédula?:'),
        choices=(('S',_('Si')),)+(('N',_('No')),),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione si tiene cédula'), 'onchange': "_has_identity_card(this.value)",
            }
        ), required = False
    )

    ## Cédula
    identity_card = IdentityCardField(
        required=False,
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ]
    )

    ## Número de teléfono
    phone = PhoneField(
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: + -")
            ),
        ]
    )

    ## Correo electrónico
    email = forms.EmailField(
        label=_("Correo Electrónico:"),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'size': '30', 'data-rule-required': 'true',
                'title': _("Indique el correo electrónico de contacto con la persona.")
            }
        ), required = False,
    )

    ## Sexo de la persona
    sex = forms.ModelChoiceField(
        label=_('Sexo:'), queryset=Sex.objects.all(), empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Sexo de la Persona'),
            }
        )
    )

    ## Fecha de nacimiento
    birthdate = forms.CharField(
        label=_('Fecha de Nacimieno:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm datepicker',
                'readonly':'true',
                'onchange':'calculate_age(this.value)',
            }
        )
    )

    ## Edad calculada a partir de la fecha de nacimiento
    age = forms.CharField(
        label=_('Edad:'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'readonly':'true',
                'title': _('Muestra la edad de la Persona'),
            }
        ),
        required = False
    )

    ## Parentesco
    family_relationship = forms.ModelChoiceField(
        label=_('Parentesco:'), queryset=FamilyRelationship.objects.all(), empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Parentesco'),
            }
        )
    )

    ## Jefe familiar
    family_head = forms.BooleanField(
        label=_('Jefe Familiar:'),
        help_text=_('Para actualizar los datos de un Jefe Familiar es necesario quitar esta selección y guardar. Hecho los cambios se puede seleccionar de nuevo si el Jefe Familiar se mantiene o se elige otro.'),
        required = False
    )

    ## Estado civil
    marital_status = forms.ModelChoiceField(
        label=_('Estado Civil:'), queryset=MaritalStatus.objects.all(), empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Estado Civil de la Persona'),
            }
        )
    )

    ## Grado de instrucción
    instruction_degree = forms.ModelChoiceField(
        label=_('Grado de Instrucción:'), queryset=InstructionDegree.objects.all(),
        empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Grado de Instrucción de la Persona'),
            }
        )
    )

    ## Misión educativa
    educational_mission = forms.ModelChoiceField(
        label=_('Misión Educativa:'), queryset=EducationalMission.objects.all(),
        empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Misión Educativa que tiene la Persona'),
            }
        )
    )

    ## Misión social
    social_mission = forms.ModelChoiceField(
        label=_('Misión Social:'), queryset=SocialMission.objects.all(),
        empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione la Misión Social que tiene la Persona'),
            }
        )
    )

    ## Profesión
    profession = forms.ModelChoiceField(
        label=_('Profesión:'), queryset=Profession.objects.all(), empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Indique la Profesión de la Persona'),
            }
        )
    )

    ## Ocupación
    occupation = forms.ModelChoiceField(
        label=_('Ocupación:'), queryset=Occupation.objects.all(), empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Indique la Ocupación de la Persona'),
            }
        )
    )

    ## Lugar de trabajo
    workplace = forms.ModelChoiceField(
        label=_('Lugar de Trabajo:'), queryset=Workplace.objects.all(), empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Indique el lugar de trabajo de la persona'),
            }
        )
    )

    ## Ingresos
    income_type = forms.ModelChoiceField(
        label=_('Tipo de Ingresos:'), queryset=IncomeType.objects.all(),
        empty_label= _('Seleccione...'),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Seleccione el Tipo de Ingreso que tiene la Persona'),
            }
        )
    )

    ## ¿Es pensionado?
    pensioner = forms.BooleanField(
        label=_('¿Es Pensionado?'),
        required = False
    )

    ## ¿Es jubilado?
    retired = forms.BooleanField(
        label=_('¿Es Jubilado?'),
        required = False
    )

    ## Deporte que practica la persona
    sports = forms.MultipleChoiceField(
        label=_('Deporte que Practica:'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Indique el Deporte que practica de la Persona'),
                'style': 'width:100%',
            }
        ),
        required = False
    )

    ## Enfermedad que presenta la persona
    diseases = forms.MultipleChoiceField(
        label=_('Enfermedad que Presenta:'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style': 'width:100%',
                'title': _("Indique la Enfermedad que Presenta la Persona"),
            }
        ),
        required = False
    )

    ## Discapacidad que presenta la persona
    disabilities = forms.MultipleChoiceField(
        label=_('Discapacidad que Presenta:'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Indique la Discapacidad que Presenta la Persona'),
                'style': 'width:100%',
            }
        ),
        required = False
    )

    ## ¿Conoce la ley de los consejos comunales?
    communal_council_law = forms.BooleanField(
        label=_('¿Ha Leído la Ley de Consejos Comunales?'),
        required = False
    )

    ## Cursos que ha realizado la persona
    courses = forms.MultipleChoiceField(
        label=_('¿Qué Cursos le Gustaría Hacer?'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': _('Indique los Cursos que le gustaría hacer'),
                'style': 'width:100%',
            }
        ),
        required = False
    )

    ## Organización comunitaria que conoce la persona
    community_organizations = forms.MultipleChoiceField(
        label = ('Organizaciones Comunitarias que conoce:'),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': _('Indique las organizaciones comunitarias que conoce'),
            'style': 'width:100%',
        }),
        required=False,
    )

    ## actividades que la persona realiza en momentos de ocio
    leisure = forms.CharField(
        label=_('¿Que hace Ud. en sus horas de ocio?'),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique lo que hace en sus horas de Ocio'),
            }
        ),
        required = False
    )

    ## ¿Cómo mejorar la comunicación en la comunidad?
    communication = forms.CharField(
        label=_('¿Qué sugiere Ud. para mejorar la comunicación en la comunidad?'),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique alguna sugerencia para mejorar la comunicación en la comunidad'),
            }
        ),
        required = False
    )

    ## Inseguridad que se presenta en la comunidad
    insecurity = forms.CharField(
        label=_('¿Qué Inseguridad Presenta la Comunidad?'),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique la inseguridad que presenta la comunidad'),
            }
        ),
        required = False
    )

    ## Comentario que la persona quiera hacer
    commentary = forms.CharField(
        label=_('Algún comentario que desee hacer en relación a las necesidades y soluciones en la comunidad'),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique algún comentario'),
            }
        ),
        required = False
    )

    ## Observación
    observation = forms.CharField(
        label=_('Observación:'),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _('Indique alguna observación que pueda tener la persona'),
            }
        ), required = False
    )

    def clean_identity_card(self):
        identity_card = self.cleaned_data['identity_card']
        if Person.objects.filter(identity_card=identity_card):
            person = Person.objects.get(identity_card=identity_card)
            communal_council_level = CommunalCouncilLevel.objects.get(communal_council=person.family_group.living_place.communal_council)
            raise forms.ValidationError(_('La persona con esta cédula ya existe, se encuentra en '+str(communal_council_level.communal_council)+', '+str(communal_council_level.communal_council.parish)+', '+ \
            str(communal_council_level.communal_council.parish.municipality)+', '+str(communal_council_level.communal_council.parish.municipality.state)+'. Administrador del Consejo Comunal: '+communal_council_level.profile.user.first_name+' '+ \
            communal_council_level.profile.user.last_name+', '+communal_council_level.profile.user.email+', '+communal_council_level.profile.phone))
        return identity_card

    def clean(self):
        """!
        Método que permite validar el formulario incluyendo varios campos

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna el formulario con los rectpectivos errores
        """

        cleaned_data = super(PersonForm, self).clean()
        family_group = self.cleaned_data['family_group']
        family_head = self.cleaned_data['family_head']

        c = 0
        if family_head:
            for p in Person.objects.filter(family_group=family_group):
                if p.family_head:
                    c= c+1
        if c >= 1:
            msg = str(_('Solo puede haber un Jefe Familiar por Grupo Familiar.'))
            self.add_error('family_head', msg)

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = Person
        exclude = [
            'family_group'
        ]

class PersonUpdateForm(PersonForm):

    def clean_identity_card(self):
        identity_card = self.cleaned_data['identity_card']
        if Person.objects.all().exclude(identity_card=identity_card):
            person = Person.objects.get(identity_card=identity_card)
            communal_council_level = CommunalCouncilLevel.objects.get(communal_council=person.family_group.living_place.communal_council)
            raise forms.ValidationError(_('La persona con esta cédula ya existe, se encuentra en '+str(communal_council_level.communal_council)+', '+str(communal_council_level.communal_council.parish)+', '+ \
            str(communal_council_level.communal_council.parish.municipality)+', '+str(communal_council_level.communal_council.parish.municipality.state)+'. Administrador del Consejo Comunal: '+communal_council_level.profile.user.first_name+' '+ \
            communal_council_level.profile.user.last_name+', '+communal_council_level.profile.user.email+', '+communal_council_level.profile.phone))
        return identity_card

    class Meta:
        model = Person
        exclude = [
            'family_group'
        ]
