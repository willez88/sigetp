from django import forms
from django.forms import (
    ModelForm, TextInput, CharField, ChoiceField, Select, BooleanField, NumberInput, ModelChoiceField
)
from django.utils.translation import ugettext_lazy as _
from .models import Vivienda, Imagen
from base.constant import (
    SERVICIO_ELECTRICO, SITUACION_SANITARIA, DISPOSICION_BASURA, TIPO_VIVIENDA, TIPO_TECHO, TIPO_PARED, TIPO_PISO, TIPO_CEMENTO,
    VALORACION, ANIMALES
)
from base.models import Estado, Municipio, Parroquia, ConsejoComunal
from encuestador.models import Encuestador
from base.fields import CoordenadaField
import datetime

class ViviendaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ViviendaForm, self).__init__(*args, **kwargs)

        lista_encuestador = [('','Selecione...')]
        for en in Encuestador.objects.all():
            lista_encuestador.append( (en.id,en.nombre+" "+en.apellido) )
        self.fields['encuestador'].choices = lista_encuestador

        self.fields['fecha_hora'].initial = datetime.datetime.now()

    encuestador = ChoiceField(
        label=_("Encuestador:"),
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione al Encuestador"),
            }
        )
    )

    fecha_hora = CharField(
        label=_("Fecha y hora:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;', 'readonly':'true',
                'title': _("Indique la Fecha y Hora del registro"),
            }
        )
    )

    numero_vivienda = CharField(
        label=_("Número de la Vivienda:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de la vivienda"),
            }
        )
    )

    servicio_electrico = ChoiceField(
        label=_("Servicio Eléctrico:"),
        choices=(('',_('Seleccione...')),)+SERVICIO_ELECTRICO,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Servicio Electrico"),
            }
        )
    )

    situacion_sanitaria = ChoiceField(
        label=_("Situación Sanitaria:"),
        choices=(('',_('Seleccione...')),)+SITUACION_SANITARIA,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Situación Sanitaria"),
            }
        )
    )

    disposicion_basura = ChoiceField(
        label=_("Disposición de la Basura:"),
        choices=(('',_('Seleccione...')),)+DISPOSICION_BASURA,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Disposición de la Basura"),
            }
        )
    )

    tipo_vivienda = ChoiceField(
        label=_("Tipo de la Vivienda:"),
        choices=(('',_('Seleccione...')),)+TIPO_VIVIENDA,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de la Vivienda"),
            }
        )
    )

    tipo_techo = ChoiceField(
        label=_("Tipo del Techo:"),
        choices=(('',_('Seleccione...')),)+TIPO_TECHO,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo del Techo"),
            }
        )
    )

    tipo_pared = ChoiceField(
        label=_("Tipo de la Pared:"),
        choices=(('',_('Seleccione...')),)+TIPO_PARED,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo de la Pared"), 'onchange': 'frizada(this.value)',
            }
        )
    )

    pared_frizada = BooleanField(
        label=_("¿La Pared está Frizada?"),
        required = False
    )

    tipo_piso = ChoiceField(
        label=_("Tipo del Piso: "),
        choices=(('',_('Seleccione...')),)+TIPO_PISO,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo del Piso"), 'onchange': 'cemento(this.value)',
            }
        )
    )

    tipo_cemento = ChoiceField(
        label=_("Tipo del Cemento: "),
        choices=(('',_('Seleccione...')),)+TIPO_CEMENTO,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione el Tipo del Cemento"),
            }
        ), required = False
    )

    condicion_vivienda = ChoiceField(
        label=_("Condición de la Vivienda:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Vivienda"),
            }
        )
    )

    condicion_techo = ChoiceField(
        label=_("Condición del Techo:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición del Techo"),
            }
        )
    )

    condicion_pared = ChoiceField(
        label=_("Condición de la Pared:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Pared"),
            }
        )
    )

    condicion_piso = ChoiceField(
        label=_("Condición del Piso:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición del Piso"),
            }
        )
    )

    condicion_ventilacion = ChoiceField(
        label=_("Condición de la Ventilación:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Ventilación"),
            }
        )
    )

    condicion_iluminacion = ChoiceField(
        label=_("Condición de la iluminación:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Condición de la Iluminación"),
            }
        )
    )

    accesibilidad_ambulatorio = ChoiceField(
        label=_("Accecibilidad al Ambulatorio:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad al Ambulatorio"),
            }
        )
    )

    accesibilidad_escuela = ChoiceField(
        label=_("Accecibilidad a la Escuela:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad a la Escuela"),
            }
        )
    )

    accesibilidad_liceo = ChoiceField(
        label=_("Accecibilidad al Liceo:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad al Liceo"),
            }
        )
    )

    accesibilidad_centro_abastecimiento = ChoiceField(
        label=_("Accecibilidad al Centro de Abastecimiento:"),
        choices=(('',_('Seleccione...')),)+VALORACION,
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Accecibilidad al Centro de Abastecimiento"),
            }
        )
    )

    numero_habitaciones = CharField(
        label=_("Número de Habitaciones:"),
        widget=NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Habitaciones"), 'size': '3', 'min':'0', 'step':'1',
            }
        )
    )

    numero_salas = CharField(
        label=_("Número de Salas:"),
        widget=NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Salas"), 'size': '3', 'min':'0', 'step':'1',
            }
        )
    )

    numero_banhos = CharField(
        label=_("Número de Baños:"),
        widget=NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Baños"), 'size': '3', 'min':'0', 'step':'1',
            }
        )
    )

    tiene_terreno = BooleanField(
        label=_("¿Tiene Terreno?"),
        widget=forms.CheckboxInput(
            attrs={
                'onclick':"""terreno($(this).is(':checked'))"""
            }
        ), required = False
    )

    metro_cuadrado = CharField(
        label=_("Metros Cuadrados:"), widget=NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados del Terreno"), 'min':'0', 'step':'0.001', 'value':'0',
        }), required=False
    )

    productivo = CharField(
        label=_("Productivo:"), widget=NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados que están Productivos"), 'min':'0', 'step':'0.001', 'value':'0',
        }), required=False
    )

    por_producir = CharField(
        label=_("Por Producir:"), widget=NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados que faltan por Producir"), 'min':'0', 'step':'0.001', 'value':'0',
        }), required=False
    )

    riesgo_rio = BooleanField(
        label=_("¿Riesgo por Ríos?"),
        required = False
    )

    riesgo_quebrada = BooleanField(
        label=_("¿Riesgo por Quebradas?"),
        required = False
    )

    riesgo_derrumbe = BooleanField(
        label=_("¿Riesgo por Derrumbes?"),
        required = False
    )

    riesgo_zona_sismica = BooleanField(
        label=_("¿Riesgo por Zona Sísmica?"),
        required = False
    )

    animales = CharField(
        label = ('Animales que tiene:'),
        widget=TextInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique los animales que tiene"),
        }),
        required=False
    )

    estado = ModelChoiceField(
        label=_("Estado"), queryset=Estado.objects.all(), empty_label=_("Seleccione..."),
        widget=Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Seleccione el estado en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Municipio','estado','pk','nombre','id_municipio')"
        })
    )

    ## Municipio en el que se encuentra ubicada la parroquia
    municipio = ModelChoiceField(
        label=_("Municipio"), queryset=Municipio.objects.all(), empty_label=_("Seleccione..."),
        widget=Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione el municipio en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','pk','nombre','id_parroquia')"
        })
    )

    ## Parroquia en donde se encuentra ubicada la dirección suministrada
    parroquia = ModelChoiceField(
        label=_("Parroquia"), queryset=Parroquia.objects.all(), empty_label=_("Seleccione..."),
        widget=Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione la parroquia en donde se encuentra ubicada"),
            'onchange': "actualizar_combo(this.value,'base','ConsejoComunal','parroquia','pk','nombre','id_consejo_comunal')"
        })
    )

    consejo_comunal = ModelChoiceField(
        label=_("Consejo Comunal"), queryset=ConsejoComunal.objects.all(), empty_label=_("Seleccione..."),
        widget=Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip', 'disabled': 'true', 'style':'width:250px;',
            'title': _("Seleccione el consejo comunal en donde se encuentra ubicado")
        })
    )

    direccion = CharField(
        label=_("Dirección:"),
        widget=TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Dirección de la vivienda"),
            }
        )
    )

    #coordenada = CoordenadaField()

    class Meta:
        model = Vivienda
        exclude = ['encuestador']

class ViviendaUpdateForm(ViviendaForm):
    def __init__(self, *args, **kwargs):
        super(ViviendaUpdateForm, self).__init__(*args, **kwargs)
        self.fields['fecha_hora'].initial = ""
        self.fields['fecha_hora'].required = False

    class Meta:
        model = Vivienda
        exclude = [
            'encuestador','fecha_hora'
        ]

class ImagenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImagenForm, self).__init__(*args, **kwargs)

        lista_vivienda = [('','Selecione...')]
        for vi in Vivienda.objects.all():
            lista_vivienda.append( (vi.id,vi.numero_vivienda+"-"+str(vi.id)) )
        self.fields['vivienda'].choices = lista_vivienda

    vivienda = forms.ChoiceField(
        label=_("Vivienda:"),
        widget=Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Vivienda"),
            }
        )
    )

    imagen = forms.ImageField()

    class Meta:
        model = Imagen
        exclude = [
            'vivienda'
        ]
