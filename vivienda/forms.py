from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Vivienda, Imagen
from base.constant import (
    SERVICIO_ELECTRICO, SITUACION_SANITARIA, DISPOSICION_BASURA, TIPO_VIVIENDA, TIPO_TECHO, TIPO_PARED, TIPO_PISO, TIPO_CEMENTO,
    VALORACION
)
from base.models import Estado, Municipio, Parroquia, ConsejoComunal
from base.fields import CoordenadaField
import datetime

class ViviendaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ViviendaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_hora'].initial = datetime.datetime.now()
        self.fields['consejo_comunal'].initial = user.perfil.consejo_comunal
        self.fields['parroquia'].initial = user.perfil.consejo_comunal.parroquia
        self.fields['municipio'].initial = user.perfil.consejo_comunal.parroquia.municipio
        self.fields['estado'].initial = user.perfil.consejo_comunal.parroquia.municipio.estado
        self.fields['rif_consejo_comunal'].initial = user.perfil.consejo_comunal.rif

        """# Si se ha seleccionado un estado establece el listado de municipios y elimina el atributo disable
        if 'estado' in self.data and self.data['estado']:
            self.fields['municipio'].widget.attrs.pop('disabled')
            self.fields['municipio'].queryset=Municipio.objects.filter(estado=self.data['estado'])

            # Si se ha seleccionado un municipio establece el listado de parroquias y elimina el atributo disable
            if 'municipio' in self.data and self.data['municipio']:
                self.fields['parroquia'].widget.attrs.pop('disabled')
                self.fields['parroquia'].queryset=Parroquia.objects.filter(municipio=self.data['municipio'])

                # Si se ha seleccionado una parroquia establece el listado de consejos comunales y elimina el atributo disable
                if 'parroquia' in self.data and self.data['parroquia']:
                    self.fields['consejo_comunal'].widget.attrs.pop('disabled')
                    self.fields['consejo_comunal'].queryset=ConsejoComunal.objects.filter(parroquia=self.data['parroquia'])"""

    fecha_hora = forms.CharField(
        label=_("Fecha y hora:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;', 'readonly':'true',
                'title': _("Indique la Fecha y Hora del registro"),
            }
        )
    )

    numero_vivienda = forms.CharField(
        label=_("Número de la Vivienda:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de la vivienda"),
            }
        )
    )

    servicio_electrico = forms.ChoiceField(
        label=_("Servicio Eléctrico:"),
        choices=(('',_('Seleccione...')),)+SERVICIO_ELECTRICO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Servicio Electrico"),
            }
        )
    )

    situacion_sanitaria = forms.ChoiceField(
        label=_("Situación Sanitaria:"),
        choices=(('',_('Seleccione...')),)+SITUACION_SANITARIA,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Situación Sanitaria"),
            }
        )
    )

    disposicion_basura = forms.ChoiceField(
        label=_("Disposición de la Basura:"),
        choices=(('',_('Seleccione...')),)+DISPOSICION_BASURA,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Disposición de la Basura"),
            }
        )
    )

    tipo_vivienda = forms.ChoiceField(
        label=_("Tipo de la Vivienda:"),
        choices=(('',_('Seleccione...')),)+TIPO_VIVIENDA,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de la Vivienda"),
            }
        )
    )

    tipo_techo = forms.ChoiceField(
        label=_("Tipo del Techo:"),
        choices=(('',_('Seleccione...')),)+TIPO_TECHO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo del Techo"),
            }
        )
    )

    tipo_pared = forms.ChoiceField(
        label=_("Tipo de la Pared:"),
        choices=(('',_('Seleccione...')),)+TIPO_PARED,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de la Pared"), 'onchange': 'frizada(this.value)',
            }
        )
    )

    pared_frizada = forms.BooleanField(
        label=_("¿La Pared está Frizada?"),
        required = False
    )

    tipo_piso = forms.ChoiceField(
        label=_("Tipo del Piso: "),
        choices=(('',_('Seleccione...')),)+TIPO_PISO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo del Piso"), 'onchange': 'cemento(this.value)',
            }
        )
    )

    tipo_cemento = forms.ChoiceField(
        label=_("Tipo del Cemento: "),
        choices=(('',_('Seleccione...')),)+TIPO_CEMENTO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo del Cemento"),
            }
        ), required = False
    )

    condicion_vivienda = forms.ChoiceField(
        label=_("Condición de la Vivienda:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Vivienda"),
            }
        )
    )

    condicion_techo = forms.ChoiceField(
        label=_("Condición del Techo:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición del Techo"),
            }
        )
    )

    condicion_pared = forms.ChoiceField(
        label=_("Condición de la Pared:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Pared"),
            }
        )
    )

    condicion_piso = forms.ChoiceField(
        label=_("Condición del Piso:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición del Piso"),
            }
        )
    )

    condicion_ventilacion = forms.ChoiceField(
        label=_("Condición de la Ventilación:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Ventilación"),
            }
        )
    )

    condicion_iluminacion = forms.ChoiceField(
        label=_("Condición de la iluminación:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Iluminación"),
            }
        )
    )

    accesibilidad_ambulatorio = forms.ChoiceField(
        label=_("Accecibilidad al Ambulatorio:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad al Ambulatorio"),
            }
        )
    )

    accesibilidad_escuela = forms.ChoiceField(
        label=_("Accecibilidad a la Escuela:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad a la Escuela"),
            }
        )
    )

    accesibilidad_liceo = forms.ChoiceField(
        label=_("Accecibilidad al Liceo:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad al Liceo"),
            }
        )
    )

    accesibilidad_centro_abastecimiento = forms.ChoiceField(
        label=_("Accecibilidad al Centro de Abastecimiento:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad al Centro de Abastecimiento"),
            }
        )
    )

    numero_habitaciones = forms.CharField(
        label=_("Número de Habitaciones:"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Habitaciones"), 'min':'0', 'step':'1',
            }
        )
    )

    numero_salas = forms.CharField(
        label=_("Número de Salas:"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Salas"), 'min':'0', 'step':'1',
            }
        )
    )

    numero_banhos = forms.CharField(
        label=_("Número de Baños:"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Baños"), 'min':'0', 'step':'1',
            }
        )
    )

    tiene_terreno = forms.BooleanField(
        label=_("¿Tiene Terreno?"),
        widget=forms.CheckboxInput(
            attrs={
                'onclick':"terreno($(this).is(':checked'))"
            }
        ), required = False
    )

    metro_cuadrado = forms.CharField(
        label=_("Metros Cuadrados:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados del Terreno"), 'min':'0', 'step':'0.01', 'value':'0',
        }), required=False
    )

    productivo = forms.CharField(
        label=_("Productivo:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados que están Productivos"), 'min':'0', 'step':'0.01', 'value':'0',
        }), required=False
    )

    por_producir = forms.CharField(
        label=_("Por Producir:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados que faltan por Producir"), 'min':'0', 'step':'0.01', 'value':'0',
        }), required=False
    )

    riesgo_rio = forms.BooleanField(
        label=_("¿Riesgo por Ríos?"),
        required = False
    )

    riesgo_quebrada = forms.BooleanField(
        label=_("¿Riesgo por Quebradas?"),
        required = False
    )

    riesgo_derrumbe = forms.BooleanField(
        label=_("¿Riesgo por Derrumbes?"),
        required = False
    )

    riesgo_zona_sismica = forms.BooleanField(
        label=_("¿Riesgo por Zona Sísmica?"),
        required = False
    )

    animales = forms.CharField(
        label = ('Animales que tiene:'),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique los animales que tiene"),
        }),
        required=False
    )

    estado = forms.CharField(
        label=_("Estado"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra el estado"),
            'readonly' : 'true',
            #'onchange': "actualizar_combo(this.value,'base','Municipio','estado','pk','nombre','id_municipio')"
        }), required=False
    )

    ## Municipio en el que se encuentra ubicada la parroquia
    municipio = forms.CharField(
        label=_("Municipio"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra el municipio"),
            'readonly' : 'true',
            #'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','pk','nombre','id_parroquia')"
        }), required=False
    )

    ## Parroquia en donde se encuentra ubicada la dirección suministrada
    parroquia = forms.CharField(
        label=_("Parroquia"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm','data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra la parroquia"),
            'readonly' : 'true',
            #'onchange': "actualizar_combo(this.value,'base','ConsejoComunal','parroquia','pk','nombre','id_consejo_comunal')"
        }), required=False
    )

    consejo_comunal = forms.CharField(
        label=_("Consejo Comunal"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm','data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra el consejo comunal"),
            'readonly':'true',
            #'onchange': "obtener_rif(this.value)",
        }), required=False
    )

    rif_consejo_comunal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm','data-toggle': 'tooltip', 'style':'width:100px;',
                'readonly':'true',
                'title': _("Muestra el RIF del Consejo Comunal"),
            }
        ), required=False
    )

    direccion = forms.CharField(
        label=_("Dirección:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Dirección de la vivienda"),
            }
        )
    )

    coordenada = CoordenadaField()

    observacion = forms.CharField(
        label=_("Observación:"),
        widget=forms.Textarea(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique alguna observación que pueda tener la vivienda"),
            }
        ), required = False
    )

    def clean(self):
        cleaned_data = super(ViviendaForm, self).clean()
        metro_cuadrado = float(self.cleaned_data['metro_cuadrado'])
        productivo = float(self.cleaned_data['productivo'])
        por_producir = float(self.cleaned_data['por_producir'])

        tipo_piso = self.cleaned_data['tipo_piso']
        tipo_cemento = self.cleaned_data['tipo_cemento']

        if metro_cuadrado != (productivo+por_producir):
            msg = str(_("El terreno productivo y por producir debe ser igual al total de metros cuadrados"))
            self.add_error('metro_cuadrado', msg)
            self.add_error('productivo', msg)
            self.add_error('por_producir', msg)

        if tipo_piso == 'CE':
            if tipo_cemento == '':
                msg = str(_("Este campo es obligatorio."))
                self.add_error('tipo_cemento', msg)

    class Meta:
        model = Vivienda
        exclude = ['user','consejo_comunal']

class ViviendaUpdateForm(ViviendaForm):
    def __init__(self, *args, **kwargs):
        super(ViviendaUpdateForm, self).__init__(*args, **kwargs)
        self.fields['fecha_hora'].required = False
        #self.fields['municipio'].widget.attrs['disabled'] = False
        #self.fields['parroquia'].widget.attrs['disabled'] = False
        #self.fields['consejo_comunal'].widget.attrs['disabled'] = False

    class Meta:
        model = Vivienda
        exclude = [
            'user','fecha_hora','consejo_comunal'
        ]

class ImagenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ImagenForm, self).__init__(*args, **kwargs)

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

    archivo_imagen = forms.ImageField()

    imagen_base64 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'invisible',
            }
        ), required=False
    )

    class Meta:
        model = Imagen
        exclude = [
            'vivienda', 'nombre'
        ]
