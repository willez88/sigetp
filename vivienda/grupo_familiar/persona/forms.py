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
## @namespace persona.forms
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
from .models import Persona
from base.constant import TIPO_TENENCIA
from vivienda.grupo_familiar.models import GrupoFamiliar
from base.fields import IdentificationCardField, PhoneField
from base.constant import (
    SEXO, PARENTESCO, ESTADO_CIVIL, GRADO_INSTRUCCION, MISION_EDUCATIVA, TIPO_INGRESO,
    ORGANIZACION_COMUNITARIA, MISION_SOCIAL
)
from django.core import validators
from usuario.models import Communal, Pollster

class PersonaForm(forms.ModelForm):
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
        super(PersonaForm, self).__init__(*args, **kwargs)
        lista_grupo_familiar = [('','Selecione...')]
        if Communal.objects.filter(profile=user.profile):
            communal = Communal.objects.get(profile=user.profile)
            for gf in GrupoFamiliar.objects.filter(vivienda__communal_council=communal.communal_council):
                lista_grupo_familiar.append( (gf.id,gf) )
        if Pollster.objects.filter(profile=user.profile):
            pollster = Pollster.objects.get(profile=user.profile)
            for gf in GrupoFamiliar.objects.filter(vivienda__user=pollster.profile.user):
                lista_grupo_familiar.append( (gf.id,gf) )
        self.fields['grupo_familiar'].choices = lista_grupo_familiar

    ## Grupo familiar al que la persona pertenece
    grupo_familiar = forms.ChoiceField(
        label=_("Grupo Familiar:"),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione El Grupo Familiar al cual pertenece la Persona"),
            }
        )
    )

    ## Nonbres
    nombre = forms.CharField(
        label=_("Nombres:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique los Nombres de la Persona"),
            }
        )
    )

    ## Apellidos
    apellido = forms.CharField(
        label=_("Apellidos:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique los Apellidos de la Persona"),
            }
        )
    )

    ## ¿Tiene cédula?
    tiene_cedula = forms.ChoiceField(
        label=_("¿Tiene Cédula?:"),
        choices=(('S',_('Si')),)+(('N',_('No')),),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:60px;',
                'title': _("Seleccione si tiene cédula"), 'onchange': "_tiene_cedula(this.value)",
            }
        ), required = False
    )

    ## Cédula
    cedula = IdentificationCardField(
        required=False,
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ]
    )

    ## Número de teléfono
    telefono = PhoneField(
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: + -")
            ),
        ]
    )

    ## Correo electrónico
    correo = forms.EmailField(
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
    sexo = forms.ChoiceField(
        label=_("Sexo:"),
        choices=(('',_('Seleccione...')),)+SEXO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Sexo de la Persona"),
            }
        )
    )

    ## Fecha de nacimiento
    fecha_nacimiento = forms.CharField(
        label=_("Fecha de Nacimieno:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm datepicker','style':'width:100%;',
                'readonly':'true',
                'onchange':'calcular_edad(this.value)',
            }
        )
    )

    ## Edad calculada a partir de la fecha de nacimiento
    edad = forms.CharField(
        label=_("Edad:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;','readonly':'true',
                'title': _("Muestra la edad de la Persona"),
            }
        ),
        required = False
    )

    ## Parentesco
    parentesco = forms.ChoiceField(
        label=_("Parentesco:"),
        choices=(('',_('Seleccione...')),)+PARENTESCO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Parentesco"),
            }
        )
    )

    ## Jefe familiar
    jefe_familiar = forms.BooleanField(
        label=_("Jefe Familiar"),
        help_text=_("Para actualizar los datos de un Jefe Familiar es necesario quitar esta selección y guardar. Hecho los cambios se puede seleccionar de nuevo si el Jefe Familiar se mantiene o se elige otro."),
        required = False
    )

    ## Estado civil
    estado_civil = forms.ChoiceField(
        label=_("Estado Civil:"),
        choices=(('',_('Seleccione...')),)+ESTADO_CIVIL,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Estado Civil de la Persona"),
            }
        )
    )

    ## Grado de instrucción
    grado_instruccion = forms.ChoiceField(
        label=_("Grado de Instrucción:"),
        choices=(('',_('Seleccione...')),)+GRADO_INSTRUCCION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Grado de Instrucción de la Persona"),
            }
        )
    )

    ## Misión educativa
    mision_educativa = forms.ChoiceField(
        label=_("Misión Educativa:"),
        choices=(('',_('Seleccione...')),)+MISION_EDUCATIVA,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Misión Educativa que tiene la Persona"),
            }
        )
    )

    ## Misión social
    mision_social = forms.ChoiceField(
        label=_("Misión Social:"),
        choices=(('',_('Seleccione...')),)+MISION_SOCIAL,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Misión Social que tiene la Persona"),
            }
        )
    )

    ## Profesión
    profesion = forms.CharField(
        label=_("Profesión:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Profesión de la Persona"),
            }
        ),
        required = False
    )

    ## Ocupación
    ocupacion = forms.CharField(
        label=_("Ocupación:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Ocupación de la Persona"),
            }
        ),
        required = False
    )

    ## Lugar de trabajo
    lugar_trabajo = forms.CharField(
        label=_("Lugar de Trabajo:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el lugar de trabajo de la persona"),
            }
        ),
        required = False
    )

    ## Ingresos
    ingreso = forms.ChoiceField(
        label=_("Tipo de Ingresos:"),
        choices=(('',_('Seleccione...')),)+TIPO_INGRESO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de Ingreso que tiene la Persona"),
            }
        )
    )

    ## ¿Es pensionado?
    pensionado = forms.BooleanField(
        label=_("¿Es Pensionado?"),
        required = False
    )

    ## ¿Es jubilado?
    jubilado = forms.BooleanField(
        label=_("¿Es Jubilado?"),
        required = False
    )

    ## Deporte que practica la persona
    deporte = forms.CharField(
        label=_("Deporte que Practica:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Deporte que practica de la Persona"),
            }
        ),
        required = False
    )

    ## Enfermedad que presenta la persona
    enfermedad = forms.CharField(
        label=_("Enfermedad que Presenta:"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Enfermedad que Presenta la Persona"),
            }
        ),
        required = False
    )

    ## Discapacidad que presenta la persona
    discapacidad = forms.CharField(
        label=_("Discapacidad que Presenta:"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Discapacidad que Presenta la Persona"),
            }
        ),
        required = False
    )

    ## ¿Conoce la ley de los consejos comunales?
    ley_consejo_comunal = forms.BooleanField(
        label=_("¿Ha Leído la Ley de Consejos Comunales?"),
        required = False
    )

    ## Cursos que ha realizado la persona
    curso = forms.CharField(
        label=_("¿Qué Cursos le Gustaría Hacer?"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique los Cursos que le gustaría hacer"),
            }
        ),
        required = False
    )

    ## Organización comunitaria que conoce la persona
    organizacion_comunitaria = forms.CharField(
        label = ('Organizaciones Comunitarias que conoce:'),
        max_length=500,
        widget=forms.TextInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique las organizaciones comunitarias que conoce"),
        }),
        required=False,
    )

    ## actividades que la persona realiza en momentos de ocio
    ocio = forms.CharField(
        label=_("¿Que hace Ud. en sus horas de ocio?"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique lo que hace en sus horas de Ocio"),
            }
        ),
        required = False
    )

    ## ¿Cómo mejorar la comunicación en la comunidad?
    mejorar_comunicacion = forms.CharField(
        label=_("¿Qué sugiere Ud. para mejorar la comunicación en la comunidad?"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique alguna sugerencia para mejorar la comunicación en la comunidad"),
            }
        ),
        required = False
    )

    ## Inseguridad que se presenta en la comunidad
    inseguridad = forms.CharField(
        label=_("¿Qué Inseguridad Presenta la Comunidad?"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la inseguridad que presenta la comunidad"),
            }
        ),
        required = False
    )

    ## Comentario que la persona quiera hacer
    comentario = forms.CharField(
        label=_("Algún comentario que desee hacer en relación a las necesidades y soluciones en la comunidad"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique algún comentario"),
            }
        ),
        required = False
    )

    ## Observación
    observacion = forms.CharField(
        label=_("Observación:"),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique alguna observación que pueda tener la persona"),
            }
        ), required = False
    )

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if Persona.objects.filter(cedula=cedula):
            persona = Persona.objects.get(cedula=cedula)
            communal = Communal.objects.get(communal_council=persona.grupo_familiar.vivienda.communal_council)
            raise forms.ValidationError(_('La persona con esta cédula ya existe, se encuentra en '+str(communal.communal_council)+', '+str(communal.communal_council.parish)+', '+ \
            str(communal.communal_council.parish.municipality)+', '+str(communal.communal_council.parish.municipality.state)+'. Administrador del Consejo Comunal: '+communal.profile.user.first_name+' '+ \
            communal.profile.user.last_name+', '+communal.profile.user.email+', '+communal.profile.phone))
        return cedula

    def clean(self):
        """!
        Método que permite validar el formulario incluyendo varios campos

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna el formulario con los rectpectivos errores
        """

        cleaned_data = super(PersonaForm, self).clean()
        grupo_familiar = self.cleaned_data['grupo_familiar']
        jefe_familiar = self.cleaned_data['jefe_familiar']

        c = 0
        if jefe_familiar:
            for p in Persona.objects.filter(grupo_familiar=grupo_familiar):
                if p.jefe_familiar:
                    c= c+1
        if c >= 1:
            msg = str(_("Solo puede haber un Jefe Familiar por Grupo Familiar."))
            self.add_error('jefe_familiar', msg)

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = Persona
        exclude = [
            'grupo_familiar'
        ]
