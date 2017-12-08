from django import forms
from base.fields import CedulaField, TelefonoField
from django.utils.translation import ugettext_lazy as _
from .models import Perfil
from django.contrib.auth.models import User
from django.core import validators

class PerfilAdminForm(forms.ModelForm):

    cedula = CedulaField(
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ],
    )

    ## Número telefónico de contacto con el usuario
    telefono = TelefonoField(
        validators=[
            validators.RegexValidator(
                r'^\+\d{3}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: + -")
            ),
        ]
    )

    class Meta:
        model = User
        fields = '__all__'

class PerfilUpdateForm(forms.ModelForm):

    username = forms.CharField(
        label=_("Nombre de Usuario:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Nombre de Usuario"),
            }
        )
    )

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

    correo = forms.EmailField(
        label=_("Correo Electrónico:"),
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'data-rule-required': 'true', 'style':'width:250px;',
                'title': _("Indique el correo electrónico de contacto con la persona.")
            }
        )
    )

    cedula = CedulaField(
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ],
    )

    telefono = TelefonoField(
        validators=[
            validators.RegexValidator(
                r'^\+\d{3}-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: + -")
            ),
        ]
    )

    consejo_comunal_temp = forms.CharField(
        label=_("Consejo Comunal:"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:100%;', 'readonly':'true',
                'title': _("Consejo Comunal que tiene asignado"),
            }
        ),
        required = False
    )

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        username = self.cleaned_data['username']

        if Perfil.objects.filter(cedula=cedula).exclude(user__username=username):
            raise forms.ValidationError(_("Este Perfil ya esta registrado"))
        return cedula

    class Meta:
        model = User
        exclude = ['perfil','consejo_comunal_temp','password','date_joined','is_superuser','is_staff','is_active','last_login']
