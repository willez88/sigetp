from django import forms
from base.fields import CedulaField, TelefonoField
from django.utils.translation import ugettext_lazy as _
from .models import Perfil
from django.contrib.auth.models import User

class PerfilAdminForm(forms.ModelForm):

    cedula = CedulaField()

    ## Número telefónico de contacto con el usuario
    telefono = TelefonoField()

    class Meta:
        model = Perfil
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

    cedula = CedulaField()

    telefono = TelefonoField()

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

    class Meta:
        model = Perfil
        exclude = ['user','consejo_comunal','consejo_comunal_temp']
