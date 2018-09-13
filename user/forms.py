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
## @namespace user.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar en la aplicación usuario
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django import forms
from base.fields import IdentityCardField, PhoneField
from django.utils.translation import ugettext_lazy as _
from .models import Profile, CommunalCouncilLevel
from django.contrib.auth.models import User
from django.core import validators
from base.models import State, Municipality, Parish, CommunalCouncil

class CommunalCouncilLevelAdminForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario del perfil usado en el panel administrativo

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 01-07-2018
    """

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
        @date 24-05-2017
        @version 1.0.0
        """

        model = User
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de perfil del usuario

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 25-06-2018
    """

    ## Username para identificar al usuario, en este caso se usa la cédula
    username = IdentityCardField(
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agregan ceros (0) si la longitud es de 7 o menos caracteres.")
            ),
        ]
    )

    ## Nombres del usuario
    first_name = forms.CharField(
        label=_("Nombres:"), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique los Nombres"),
            }
        )
    )

    ## Apellidos del usuario
    last_name = forms.CharField(
        label=_("Apellidos:"), max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique los Apellidos"),
            }
        )
    )

    ## Correo del usuario
    email = forms.EmailField(
        label=_("Correo Electrónico:"), max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'data-toggle': 'tooltip',
                'title': _("Indique el correo electrónico de contacto")
            }
        )
    )

    ## Teléfono del usuario
    phone = PhoneField(
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números.")
            ),
        ]
    )

    ## Clave de acceso del usuario
    password = forms.CharField(
        label=_("Contraseña:"), max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique una contraseña de aceso al sistema")
            }
        )
    )

    ## Confirmación de clave de acceso del usuario
    confirm_password = forms.CharField(
        label=_("Confirmar Contraseña:"), max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique nuevamente la contraseña de aceso al sistema")
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError(_("El correo ya esta registrado"))
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError(_("La contraseña no es la misma"))
        return confirm_password

    #class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 25-06-2018
        """

        #model = User
        #exclude = ['profile','date_joined']

class CommunalCouncilLevelUpdateForm(ProfileForm):

    def __init__(self, *args, **kwargs):
        super(CommunalCouncilLevelUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirm_password'].required = False
        self.fields['password'].widget.attrs['disabled'] = True
        self.fields['confirm_password'].widget.attrs['disabled'] = True

    communal_council = forms.CharField(
        label=_("Consejo Comunal:"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'readonly':'true',
                'style': 'width:100%',
                'title': _("Consejo Comunal que tiene asignado"),
            }
        ),required = False
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(_("El correo ya esta registrado "))
        return email

    def clean_confirm_password(self):
        pass

    class Meta:
        model = Profile
        exclude = [
            'user','communal_council','password','confirm_password'
        ]

class PollsterForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PollsterForm, self).__init__(*args, **kwargs)
        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=user.profile)
            self.fields['communal_council'].initial = communal_council_level.communal_council

    communal_council = forms.CharField(
        label=_("Consejo Comunal:"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'readonly':'true',
                'style': 'width:100%',
                'title': _("Consejo Comunal que tiene asignado"),
            }
        ),required = False
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 25-06-2018
        """

        model = User
        exclude = [
            'date_joined','last_login','is_active','is_superuser','is_staff','communal_council'
        ]

class PollsterUpdateForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super(PollsterUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirm_password'].required = False
        self.fields['password'].widget.attrs['disabled'] = True
        self.fields['confirm_password'].widget.attrs['disabled'] = True

    communal_council = forms.CharField(
        label=_("Consejo Comunal:"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'readonly':'true',
                'style': 'width:100%',
                'title': _("Consejo Comunal que tiene asignado"),
            }
        ),required = False
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(_("El correo ya esta registrado "))
        return email

    def clean_confirm_password(self):
        pass

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 25-06-2018
        """

        model = Profile
        exclude = [
            'user','password','confirm_password','communal_council'
        ]

class PollsterStatusForm(forms.ModelForm):

    is_active = forms.BooleanField(
        label=_("¿Está Activo?"), required=False
    )

    class Meta:

        model = User
        exclude = [
            'username','first_name','last_name','email','password','date_joined',
            'last_login','is_superuser','is_staff',
        ]
