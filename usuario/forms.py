from django import forms
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField, ChoiceField, Select, PasswordInput
)
from base.fields import CedulaField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import Perfil

class PerfilAdminForm(ModelForm):

    cedula = CedulaField()

    ## Número telefónico de contacto con el usuario
    telefono = CharField(
        label=_("Teléfono:"),
        max_length=18,
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '(+058)-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip',
                'title': _("Indique el número telefónico de contacto con el usuario"), 'data-mask': '(+000)-000-0000000'
            }
        ),
        help_text=_("(país)-área-número")
    )

    """def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if Perfil.objects.filter(cedula=cedula):
            raise forms.ValidationError(_("El Usuario ya se encuentra registrado"))
        return cedula"""

    class Meta:
        model = Perfil
        fields = '__all__'

class AutenticarForm(forms.Form):

    username = CharField(
        label=_("Usuario:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': _("usuario"), 'data-toggle': 'tooltip',
                'title': _("Indique El nombre de Usuario"),
            }
        )
    )

    password = CharField(
        label=_("Contraseña"), max_length=30, widget=PasswordInput(attrs={
            'class': 'form-control input-sm', 'placeholder': _("contraseña de acceso"), 'data-toggle': 'tooltip',
            'title': _("Indique la contraseña de acceso al sistema"),
        })
    )

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(AutenticarForm, self).__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super(AutenticarForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            if not User.objects.filter(username=username):
                msg = "El Usuario no esta registrado"
                self.add_error('username', msg)

            if User.objects.filter(username=username) and not User.objects.get(username=username).check_password(password):
                msg = "Contraseña incorrecta"
                self.add_error('password', msg)

    def get_user(self):
        return self.user_cache
