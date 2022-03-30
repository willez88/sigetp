from base.fields import IdentityCardField, PhoneField
from base.models import (
    CommunityOrganization, Course, Disability, Disease, EducationalMission,
    Gender, IncomeType, InstructionDegree, MaritalStatus, Occupation,
    Profession, Relationship, SocialMission, Sport, Workplace,
)
from django import forms
from django.core import validators
from living_place.family_group.models import FamilyGroup
from user.models import CommunalCouncilLevel, Pollster

from .models import Person


class PersonForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de persona

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Retorna el formulario con una configuración inicializada de
            forma manual
        """

        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        family_group_list = [('', 'Selecione...')]
        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=user.profile
            )
            ccl = communal_council_level.communal_council
            for fg in FamilyGroup.objects.filter(
                living_place__communal_council=ccl
            ):
                family_group_list.append((fg.id, fg))
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            for fg in FamilyGroup.objects.filter(
                living_place__user=pollster.profile.user
            ):
                family_group_list.append((fg.id, fg))
        self.fields['family_group'].choices = family_group_list

        sports_list = []
        for sp in Sport.objects.all():
            sports_list.append((sp.id, sp))
        self.fields['sports'].choices = sports_list

        diseases_list = []
        for di in Disease.objects.all():
            diseases_list.append((di.id, di))
        self.fields['diseases'].choices = diseases_list

        disabilities_list = []
        for dis in Disability.objects.all():
            disabilities_list.append((dis.id, dis))
        self.fields['disabilities'].choices = disabilities_list

        courses_list = []
        for co in Course.objects.all():
            courses_list.append((co.id, co))
        self.fields['courses'].choices = courses_list

        community_organizations_list = []
        for com in CommunityOrganization.objects.all():
            community_organizations_list.append((com.id, com))
        self.fields[
            'community_organizations'
        ].choices = community_organizations_list

    # Grupo familiar al que la persona pertenece
    family_group = forms.ChoiceField(
        label='Grupo Familiar:',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione El Grupo Familiar al cual pertenece \
                    la Persona',
            }
        )
    )

    # Nonbres
    first_name = forms.CharField(
        label='Nombres:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique los Nombres de la Persona',
            }
        )
    )

    # Apellidos
    last_name = forms.CharField(
        label='Apellidos:',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique los Apellidos de la Persona',
            }
        )
    )

    # ¿Tiene cédula?
    has_identity_card = forms.ChoiceField(
        label='¿Tiene Cédula?:',
        choices=(('S', 'Si'),) + (('N', 'No'),),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione si tiene cédula',
                'onchange': "_has_identity_card(this.value)",
            }
        ), required=False
    )

    # Cédula
    identity_card = IdentityCardField(
        required=False,
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                'Introduzca un número de cédula válido. Solo se permiten \
                    números y una longitud de 8 carácteres. Se agrega un 0 si \
                    la longitud es de 7 carácteres.'
            ),
        ]
    )

    # Número de teléfono
    phone = PhoneField(
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                'Número telefónico inválido. Solo se permiten números y los \
                    símbolos: + -'
            ),
        ]
    )

    # Correo electrónico
    email = forms.EmailField(
        label='Correo Electrónico:',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask',
                'placeholder': 'Correo de contacto',
                'data-toggle': 'tooltip', 'size': '30',
                'data-rule-required': 'true',
                'title': 'Indique el correo electrónico de contacto con \
                    la persona.'
            }
        ), required=False,
    )

    # Género
    gender = forms.ModelChoiceField(
        label='Género:', queryset=Gender.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Sexo de la Persona',
            }
        )
    )

    # Fecha de nacimiento
    birthdate = forms.CharField(
        label='Fecha de Nacimieno:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm datepicker',
                'readonly': 'true',
                'onchange': 'calculate_age(this.value)',
            }
        )
    )

    # Edad calculada a partir de la fecha de nacimiento
    age = forms.CharField(
        label='Edad:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'readonly': 'true',
                'title': 'Muestra la edad de la Persona',
            }
        ),
        required=False
    )

    # Parentesco
    relationship = forms.ModelChoiceField(
        label='Parentesco:', queryset=Relationship.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Parentesco',
            }
        )
    )

    # Jefe familiar
    family_head = forms.BooleanField(
        label='Jefe Familiar:',
        help_text='Para actualizar los datos de un Jefe Familiar es necesario \
            quitar esta selección y guardar. Hecho los cambios se puede \
            seleccionar de nuevo si el Jefe Familiar se mantiene o \
            se elige otro.',
        required=False
    )

    # Estado civil
    marital_status = forms.ModelChoiceField(
        label='Estado Civil:', queryset=MaritalStatus.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Estado Civil de la Persona',
            }
        )
    )

    # Grado de instrucción
    instruction_degree = forms.ModelChoiceField(
        label='Grado de Instrucción:',
        queryset=InstructionDegree.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Grado de Instrucción de la Persona',
            }
        )
    )

    # Misión educativa
    educational_mission = forms.ModelChoiceField(
        label='Misión Educativa:', queryset=EducationalMission.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Misión Educativa que tiene la Persona',
            }
        )
    )

    # Misión social
    social_mission = forms.ModelChoiceField(
        label='Misión Social:', queryset=SocialMission.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione la Misión Social que tiene la Persona',
            }
        )
    )

    # Profesión
    profession = forms.ModelChoiceField(
        label='Profesión:', queryset=Profession.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Indique la Profesión de la Persona',
            }
        )
    )

    # Ocupación
    occupation = forms.ModelChoiceField(
        label='Ocupación:', queryset=Occupation.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Indique la Ocupación de la Persona',
            }
        )
    )

    # Lugar de trabajo
    workplace = forms.ModelChoiceField(
        label='Lugar de Trabajo:', queryset=Workplace.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Indique el lugar de trabajo de la persona',
            }
        )
    )

    # Ingresos
    income_type = forms.ModelChoiceField(
        label='Tipo de Ingresos:', queryset=IncomeType.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Seleccione el Tipo de Ingreso que tiene la Persona',
            }
        )
    )

    # ¿Es pensionado?
    pensioner = forms.BooleanField(
        label='¿Es Pensionado?',
        required=False
    )

    # ¿Es jubilado?
    retired = forms.BooleanField(
        label='¿Es Jubilado?',
        required=False
    )

    # Deporte que practica la persona
    sports = forms.MultipleChoiceField(
        label='Deporte que Practica:',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Indique el Deporte que practica de la Persona',
                'style': 'width:100%',
            }
        ),
        required=False
    )

    # Enfermedad que presenta la persona
    diseases = forms.MultipleChoiceField(
        label='Enfermedad que Presenta:',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'style': 'width:100%',
                'title': 'Indique la Enfermedad que Presenta la Persona',
            }
        ),
        required=False
    )

    # Discapacidad que presenta la persona
    disabilities = forms.MultipleChoiceField(
        label='Discapacidad que Presenta:',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Indique la Discapacidad que Presenta la Persona',
                'style': 'width:100%',
            }
        ),
        required=False
    )

    # ¿Conoce la ley de los consejos comunales?
    communal_council_law = forms.BooleanField(
        label='¿Ha Leído la Ley de Consejos Comunales?',
        required=False
    )

    # Cursos que ha realizado la persona
    courses = forms.MultipleChoiceField(
        label='¿Qué Cursos le Gustaría Hacer?',
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip',
                'title': 'Indique los Cursos que le gustaría hacer',
                'style': 'width:100%',
            }
        ),
        required=False
    )

    # Organización comunitaria que conoce la persona
    community_organizations = forms.MultipleChoiceField(
        label='Organizaciones Comunitarias que conoce:',
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': 'Indique las organizaciones comunitarias que conoce',
            'style': 'width:100%',
        }),
        required=False,
    )

    # actividades que la persona realiza en momentos de ocio
    leisure = forms.CharField(
        label='¿Que hace Ud. en sus horas de ocio?',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique lo que hace en sus horas de Ocio',
            }
        ),
        required=False
    )

    # ¿Cómo mejorar la comunicación en la comunidad?
    communication = forms.CharField(
        label='¿Qué sugiere Ud. para mejorar la comunicación en la comunidad?',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique alguna sugerencia para mejorar la \
                    comunicación en la comunidad',
            }
        ),
        required=False
    )

    # Inseguridad que se presenta en la comunidad
    insecurity = forms.CharField(
        label='¿Qué Inseguridad Presenta la Comunidad?',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique la inseguridad que presenta la comunidad',
            }
        ),
        required=False
    )

    # Comentario que la persona quiera hacer
    commentary = forms.CharField(
        label='Algún comentario que desee hacer en relación a las necesidades \
            y soluciones en la comunidad',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique algún comentario',
            }
        ),
        required=False
    )

    # Observación
    observation = forms.CharField(
        label='Observación:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique alguna observación que pueda tener la \
                    persona',
            }
        ), required=False
    )

    def clean_identity_card(self):
        identity_card = self.cleaned_data['identity_card']
        if Person.objects.filter(identity_card=identity_card):
            person = Person.objects.get(identity_card=identity_card)
            p = person.family_group.living_place.communal_council
            communal_council_level = CommunalCouncilLevel.objects.get(
                communal_council=p
            )
            cc = communal_council_level.communal_council
            parish = communal_council_level.communal_council.parish
            municipality = communal_council_level.communal_council.parish.\
                municipality
            state = communal_council_level.communal_council.parish.\
                municipality.state
            first_name = communal_council_level.profile.user.first_name
            last_name = communal_council_level.profile.user.last_name
            email = communal_council_level.profile.user.email
            phone = communal_council_level.profile.phone
            raise forms.ValidationError(
                'La persona con esta cédula ya existe, se encuentra en ' +
                str(cc) + ', ' + str(parish) + ', ' + str(municipality) +
                ', ' + str(state) + '. Administrador del Consejo Comunal: ' +
                first_name + ' ' + last_name + ', ' + email + ', ' + phone
            )
        return identity_card

    def clean(self):
        """!
        Método que permite validar el formulario incluyendo varios campos

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna el formulario con los rectpectivos errores
        """

        cleaned_data = super().clean()
        family_group = self.cleaned_data['family_group']
        family_head = self.cleaned_data['family_head']

        c = 0
        if family_head:
            for p in Person.objects.filter(family_group=family_group):
                if p.family_head:
                    c = c + 1
        if c >= 1:
            self.add_error(
                'family_head',
                'Solo puede haber un Jefe Familiar por Grupo Familiar.'
            )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
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
            p = person.family_group.living_place.communal_council
            communal_council_level = CommunalCouncilLevel.objects.get(
                communal_council=p
            )
            cc = communal_council_level.communal_council
            parish = communal_council_level.communal_council.parish
            municipality = communal_council_level.communal_council.parish.\
                municipality
            state = communal_council_level.communal_council.parish.\
                municipality.state
            first_name = communal_council_level.profile.user.first_name
            last_name = communal_council_level.profile.user.last_name
            email = communal_council_level.profile.user.email
            phone = communal_council_level.profile.phone
            raise forms.ValidationError(
                'La persona con esta cédula ya existe, se encuentra en ' +
                str(cc)+', ' + str(parish) + ', ' + str(municipality) + ', ' +
                str(state) + '. Administrador del Consejo Comunal: ' +
                first_name + ' ' + last_name + ', ' + email + ', ' + phone
            )
        return identity_card

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        model = Person
        exclude = [
            'family_group'
        ]
