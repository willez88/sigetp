from django import forms
from base.fields import CedulaField, TelefonoField
from django.utils.translation import ugettext_lazy as _
from .models import Perfil

class PerfilAdminForm(forms.ModelForm):

    cedula = CedulaField()

    ## Número telefónico de contacto con el usuario
    telefono = TelefonoField()

    """def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        if Perfil.objects.filter(cedula=cedula):
            raise forms.ValidationError(_("El Usuario ya se encuentra registrado"))
        return cedula"""

    class Meta:
        model = Perfil
        fields = '__all__'
