from django import forms
from django.forms import Select, TextInput, NumberInput, EmailInput
from django.utils.translation import ugettext_lazy as _
from .models import Persona
from base.constant import TIPO_TENENCIA
from encuestador.vivienda.grupo_familiar.models import GrupoFamiliar
from base.fields import CedulaField
from base.constant import SEXO, PARENTESCO, ESTADO_CIVIL, GRADO_INSTRUCCION, MISION_EDUCATIVA, TIPO_INGRESO, ORGANIZACION_COMUNITARIA

class PersonaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        lista_grupo_familiar = [('','Selecione...')]
        for gf in GrupoFamiliar.objects.all():
            lista_grupo_familiar.append( (gf.id,gf.apellido_familia+"-"+str(gf.id)) )
        self.fields['grupo_familiar'].choices = lista_grupo_familiar
        self.fields['tiene_cedula'].initial = True

    grupo_familiar = forms.ChoiceField(
        label=_("Grupo Familiar:"),
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione El Grupo Familiar al cual pertenece la Persona"),
            }
        )
    )

    nombre = forms.CharField(
        label=_("Nombres:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique los Nombres de la Persona"),
            }
        )
    )

    apellido = forms.CharField(
        label=_("Apellidos:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique los Apellidos de la Persona"),
            }
        )
    )

    tiene_cedula = forms.ChoiceField(
        label=_("¿Tiene Cédula?"),
        choices=((True,'Si'), (False,'No')),
        widget=forms.CheckboxInput(attrs={
                'class': 'form-control',
                'onclick': "_tiene_cedula($(this).is(':checked'))",
            }
        ),
        required = False
    )

    cedula = CedulaField(required=False)

    telefono = forms.CharField(
        label=_("Teléfono:"),
        max_length=20,
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '(058)-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'size': '15',
                'title': _("Indique el número telefónico de contacto con el usuario"), 'data-mask': '(000)-000-0000000'
            }
        ),
        help_text=_("(país)-área-número"),
        required = False,
    )

    correo = forms.EmailField(
        label=_("Correo Electrónico:"),
        max_length=100,
        widget=EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'size': '30', 'data-rule-required': 'true',
                'title': _("Indique el correo electrónico de contacto con el usuario. "
                           "No se permiten correos de hotmail")
            }
        ), required = False,
    )

    sexo = forms.ChoiceField(
        label=_("Sexo:"),
        choices=(('',_('Seleccione...')),)+SEXO,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Sexo de la Persona"),
            }
        )
    )

    fecha_nacimiento = forms.CharField(
        label=_("Fecha de Nacimieno:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Fecha de Nacimiento de la Persona"), 'onblur':'calcular_edad(this.value)',
            }
        )
    )

    edad = forms.CharField(
        label=_("Edad:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;', 'readonly':'true',
                'title': _("Muestra la edad de la Persona"),
            }
        ),
        required = False
    )

    parentesco = forms.ChoiceField(
        label=_("Parentesco:"),
        choices=(('',_('Seleccione...')),)+PARENTESCO,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Parentesco"),
            }
        )
    )

    estado_civil = forms.ChoiceField(
        label=_("Estado Civil:"),
        choices=(('',_('Seleccione...')),)+ESTADO_CIVIL,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Estado Civil de la Persona"),
            }
        )
    )

    grado_instruccion = forms.ChoiceField(
        label=_("Grado de Instrucción:"),
        choices=(('',_('Seleccione...')),)+GRADO_INSTRUCCION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Grado de Instrucción de la Persona"),
            }
        )
    )

    mision_educativa = forms.ChoiceField(
        label=_("Misión Educativa:"),
        choices=(('',_('Seleccione...')),)+MISION_EDUCATIVA,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Misión Educativa que tiene la Persona"),
            }
        )
    )

    profesion = forms.CharField(
        label=_("Profesión:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Profesión de la Persona"),
            }
        ),
        required = False
    )

    ocupacion = forms.CharField(
        label=_("Ocupación:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Ocupación de la Persona"),
            }
        ),
        required = False
    )

    ingreso = forms.ChoiceField(
        label=_("Tipo de Ingresos:"),
        choices=(('',_('Seleccione...')),)+TIPO_INGRESO,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de Ingreso que tiene la Persona"),
            }
        )
    )

    deporte = forms.CharField(
        label=_("Deporte que Practica:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Deporte que practica de la Persona"),
            }
        ),
        required = False
    )

    enfermedad = forms.CharField(
        label=_("Enfermedad que Presenta:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Enfermedad que Presenta la Persona"),
            }
        ),
        required = False
    )

    discapacidad = forms.CharField(
        label=_("Discapacidad que Presenta:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Discapacidad que Presenta la Persona"),
            }
        ),
        required = False
    )

    ley_consejo_comunal = forms.BooleanField(
        label=_("¿Ha Leído la Ley de Consejos Comunales?"),
        required = False
    )

    curso = forms.CharField(
        label=_("¿Qué Cursos le Gustaría Hacer?"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique los Cursos que le gustaría hacer"),
            }
        ),
        required = False
    )

    organizacion_comunitaria = forms.MultipleChoiceField(
        label = ('Organizaciones Comunitarias que conoce:'),
        choices = ORGANIZACION_COMUNITARIA,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    ocio = forms.CharField(
        label=_("¿Que hace Ud. en sus horas de ocio?"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique lo que hace en sus horas de Ocio"),
            }
        ),
        required = False
    )

    mejorar_comunicacion = forms.CharField(
        label=_("¿Qué sugiere Ud. para mejorar la comunicación en la comunidad?"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique alguna sugerencia para mejorar la comunicación en la comunidad"),
            }
        ),
        required = False
    )

    inseguridad = forms.CharField(
        label=_("¿Qué Inseguridad Presenta la Comunidad?"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la inseguridad que presenta la comunidad"),
            }
        ),
        required = False
    )

    comentario = forms.CharField(
        label=_("Algún comentario que desee hacer en relación a las necesidades y soluciones en la comunidad"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique algún comentario"),
            }
        ),
        required = False
    )

    class Meta:
        model = Persona
        exclude = [
            'grupo_familiar'
        ]
