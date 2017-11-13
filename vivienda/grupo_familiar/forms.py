from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import GrupoFamiliar
from base.constant import TIPO_TENENCIA
from vivienda.models import Vivienda

class GrupoFamiliarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(GrupoFamiliarForm, self).__init__(*args, **kwargs)

        lista_vivienda = [('','Selecione...')]
        for vi in Vivienda.objects.filter(user=user):
            lista_vivienda.append( (vi.id,vi.numero_vivienda+"-"+str(vi.id)) )
        self.fields['vivienda'].choices = lista_vivienda

    vivienda = forms.ChoiceField(
        label=_("Vivienda:"),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Vivienda"),
            }
        )
    )

    apellido_familia = forms.CharField(
        label=_("Apellidos de la Familia:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Apellido de la Familia"),
            }
        )
    )

    familia_beneficiada = forms.BooleanField(
        label=_("¿La Familia ha sido beneficiada por el CLAP?"),
        required = False,
    )

    tenencia = forms.ChoiceField(
        label=_("Tipo de Tenencia de la Vivienda:"),
        choices=(('',_('Seleccione...')),)+TIPO_TENENCIA,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de Tenencia de la Vivienda"), 'onchange': '__tenencia(this.value)',
            }
        )
    )

    alquilada = forms.CharField(
        label=_("Tiempo Alquilado:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique el tiempo que tiene como alquilado"), 'min':'0', 'step':'1', 'value':'0',
        }), required=False
    )

    pasaje = forms.BooleanField(
        label=_("¿Cree Ud. que se deba consultar a las comunidades para los precios del pasaje?"),
        required = False,
    )

    observacion = forms.CharField(
        label=_("Observación:"),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique alguna observación que pueda tener el grupo familiar"),
            }
        ), required = False
    )

    class Meta:
        model = GrupoFamiliar
        exclude = [
            'vivienda'
        ]
