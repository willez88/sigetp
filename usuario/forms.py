from django import forms
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField, ChoiceField, Select, PasswordInput
)
from base.fields import CedulaField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import Perfil

class PerfilAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PerfilAdminForm, self).__init__(*args, **kwargs)

        lista_user = [('','Selecione...')]
        for us in User.objects.all():
            lista_user.append( (us.id,us.first_name+" "+us.last_name) )
        self.fields['user'].choices = lista_user

    user = ChoiceField(
        label=_("Usuario:"),
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Usuario"),
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

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if Perfil.objects.filter(cedula=cedula):
            raise forms.ValidationError(_("El Usuario ya se encuentra registrado"))
        return cedula

    class Meta:
        model = Perfil
        exclude = [
            'fecha_modpass'
        ]

class AutenticarForm(forms.Form):

    usuario = CharField(
        label=_("Usuario:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("usuario"), 'data-toggle': 'tooltip',
                'title': _("Indique El nombre de Usuario"),
            }
        )
    )

    clave = CharField(
        label=_("Contraseña"), max_length=30, widget=PasswordInput(attrs={
            'class': 'form-control input-sm', 'placeholder': _("contraseña de acceso"), 'data-toggle': 'tooltip',
            'title': _("Indique la contraseña de acceso al sistema"), 'size': '28',
        })
    )

    def clean(self):
        cleaned_data = super(AutenticarForm, self).clean()
        usuario = self.cleaned_data['usuario']
        clave = self.cleaned_data['clave']

        if not User.objects.filter(username=usuario):
            msg = "El Usuario no esta registrado"
            self.add_error('usuario', msg)

        if User.objects.filter(username=usuario) and not User.objects.get(username=usuario).check_password(clave):
            msg = "Contraseña incorrecta"
            self.add_error('clave', msg)

