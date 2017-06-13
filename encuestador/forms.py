from django import forms
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField
)
from base.fields import CedulaField
from django.utils.translation import ugettext_lazy as _
from .models import Encuestador

class EncuestadorForm(ModelForm):
    nombre = CharField(
        label=_("Nombres:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Nombres del Encuestador"),
            }
        )
    )

    apellido = CharField(
        label=_("Apellidos:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Apellidos del Encuestador"),
            }
        )
    )

    cedula = CedulaField()

    ## Número telefónico de contacto con el usuario
    telefono = CharField(
        label=_("Teléfono:"),
        max_length=20,
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '(058)-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip', 'size': '15',
                'title': _("Indique el número telefónico de contacto con el usuario"), 'data-mask': '(000)-000-0000000'
            }
        ),
        help_text=_("(país)-área-número")
    )

    correo = EmailField(
        label=_("Correo Electrónico: "),
        max_length=100,
        widget=EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask', 'placeholder': _("Correo de contacto"),
                'data-toggle': 'tooltip', 'size': '30', 'data-rule-required': 'true',
                'title': _("Indique el correo electrónico de contacto con el usuario. "
                           "No se permiten correos de hotmail")
            }
        )
    )

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if Encuestador.objects.filter(cedula=cedula):
            raise forms.ValidationError(_("El Encuestador ya se encuentra registrado"))
        return cedula

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if User.objects.filter(email=correo):
            raise forms.ValidationError(_("El correo ya esta registrado"))
        return correo

    class Meta:
        model = Encuestador
        fields = '__all__'

