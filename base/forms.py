from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Estado, Municipio, Parroquia, ConsejoComunal
from .fields import RifField

class ConsejoComunalAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ConsejoComunalAdminForm, self).__init__(*args, **kwargs)

        lista_vivienda = [('','Selecione...')]

    rif = RifField()

    nombre = forms.CharField(
        label=_("Nombre del RIF"),
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': _("Indique el Nombre del RIF"),
            }
        )
    )

    estado = forms.ModelChoiceField(
        label=_("Estado"), queryset=Estado.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Seleccione el estado en donde se encuentra ubicada"),
            #'onchange': "actualizar_combo(this.value,'base','Municipio','estado','pk','nombre','id_municipio')"
        })
    )

    ## Municipio en el que se encuentra ubicada la parroquia
    municipio = forms.ModelChoiceField(
        label=_("Municipio"), queryset=Municipio.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione el municipio en donde se encuentra ubicada"),
            #'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','pk','nombre','id_parroquia')"
        })
    )

    ## Parroquia en donde se encuentra ubicada la dirección suministrada
    parroquia = forms.ModelChoiceField(
        label=_("Parroquia"), queryset=Parroquia.objects.all(), empty_label=_("Seleccione..."),
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true',
            'title': _("Seleccione la parroquia en donde se encuentra ubicada"),
        })
    )

    class Meta:
        model = ConsejoComunal
        exclude = [
            'estado', 'municipio'
        ]
