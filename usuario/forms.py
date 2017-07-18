from django import forms
from base.fields import CedulaField
from django.utils.translation import ugettext_lazy as _
from .models import Perfil

class PerfilAdminForm(forms.ModelForm):

    cedula = CedulaField()

    ## Número telefónico de contacto con el usuario
    telefono = forms.CharField(
        label=_("Teléfono:"),
        max_length=18,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '(+058)-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip',
                'title': _("Indique el número telefónico de contacto con el usuario"), 'data-mask': '(+000)-000-0000000',
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
