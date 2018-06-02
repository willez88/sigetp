"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CENDITEL (2017)

Autores: William Páez

La Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres (CENDITEL),
ente adscrito al Ministerio del Poder Popular para Educación Universitaria, Ciencia y Tecnología
(MPPEUCT), concede permiso para usar, copiar, modificar y distribuir libremente y sin fines
comerciales el "Software - Registro de bienes de CENDITEL", sin garantía
alguna, preservando el reconocimiento moral de los autores y manteniendo los mismos principios
para las obras derivadas, de conformidad con los términos y condiciones de la licencia de
software de la Fundación CENDITEL.

El software es una creación intelectual necesaria para el desarrollo económico y social
de la nación, por tanto, esta licencia tiene la pretensión de preservar la libertad de
este conocimiento para que contribuya a la consolidación de la soberanía nacional.

Cada vez que copie y distribuya el "Software - Registro de bienes de CENDITEL"
debe acompañarlo de una copia de la licencia. Para más información sobre los términos y condiciones
de la licencia visite la siguiente dirección electrónica:
http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/
"""
## @namespace vivienda.forms
#
# Contiene las clases, atributos y métodos para los formularios a implementar en la aplicación vivienda
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

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
    """!
    Clase que contiene los campos del formulario de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        user = kwargs.pop('user')
        super(ViviendaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_hora'].initial = datetime.datetime.now()
        self.fields['consejo_comunal'].initial = user.perfil.consejo_comunal
        self.fields['parroquia'].initial = user.perfil.consejo_comunal.parroquia
        self.fields['municipio'].initial = user.perfil.consejo_comunal.parroquia.municipio
        self.fields['estado'].initial = user.perfil.consejo_comunal.parroquia.municipio.estado
        self.fields['rif_consejo_comunal'].initial = user.perfil.consejo_comunal.rif

    ## Fecha y hora del registro de la vivienda
    fecha_hora = forms.CharField(
        label=_("Fecha y hora:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;', 'readonly':'true',
                'title': _("Indique la Fecha y Hora del registro"),
            }
        )
    )

    ## Número de identificación de la vivienda
    numero_vivienda = forms.CharField(
        label=_("Número de la Vivienda:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de la vivienda"),
            }
        )
    )

    ## Servicio eléctrico usado en la vivienda
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

    ## Situación sanitaria presentada en la vivienda
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

    ## Disposicíon de la basura usada en la vivienda
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

    ## Tipo de vivienda
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

    ## Tipo de techo de la vivienda
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

    ## Tipo de pared de la vivienda
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

    ## Pared frizada
    pared_frizada = forms.BooleanField(
        label=_("¿La Pared está Frizada?"),
        required = False
    )

    ## Tipo del piso de la vivienda
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

    ## Tipo de cemento del piso de la vivienda
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

    ## Condición presentada en la vivienda
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

    ## Condición del techo de la vivienda
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

    ## Condición de la pared
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

    ## Condición del piso
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

    ## Condición de la ventilación
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

    ## Condición de la iluminación
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

    ## Accesibilidad al ambulatorio
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

    ## Accesibilidad a la escuela
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

    ## Accesibilidad al liceo
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

    ## Accesibilidad al centro de abastecimiento
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

    ## Número de habitaciones
    numero_habitaciones = forms.CharField(
        label=_("Número de Habitaciones:"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Habitaciones"), 'min':'0', 'step':'1',
            }
        )
    )

    ## Número de salas
    numero_salas = forms.CharField(
        label=_("Número de Salas:"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Salas"), 'min':'0', 'step':'1',
            }
        )
    )

    ## Número de baños
    numero_banhos = forms.CharField(
        label=_("Número de Baños:"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el Número de Baños"), 'min':'0', 'step':'1',
            }
        )
    )

    ## ¿Tiene terreno la vivienda?
    tiene_terreno = forms.BooleanField(
        label=_("¿Tiene Terreno?"),
        widget=forms.CheckboxInput(
            attrs={
                'onclick':"terreno($(this).is(':checked'))"
            }
        ), required = False
    )

    ## Metros cuadrados de terreno que tiene la vivienda
    metro_cuadrado = forms.CharField(
        label=_("Metros Cuadrados:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados del Terreno"), 'min':'0', 'step':'0.01', 'value':'0',
        }), required=False
    )

    ## Metros cuadrados de terreno que la vivienda tiene productivos
    productivo = forms.CharField(
        label=_("Productivo:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados que están Productivos"), 'min':'0', 'step':'0.01', 'value':'0',
        }), required=False
    )

    ## Metros cuadrados de terreno que la vivienda tiene sin producir
    por_producir = forms.CharField(
        label=_("Por Producir:"), widget=forms.NumberInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique la cantidad de Metros Cuadrados que faltan por Producir"), 'min':'0', 'step':'0.01', 'value':'0',
        }), required=False
    )

    ## Riesgo por río
    riesgo_rio = forms.BooleanField(
        label=_("¿Riesgo por Ríos?"),
        required = False
    )

    ## Riesgo por quebrada
    riesgo_quebrada = forms.BooleanField(
        label=_("¿Riesgo por Quebradas?"),
        required = False
    )

    ## riesgo por derrumbe
    riesgo_derrumbe = forms.BooleanField(
        label=_("¿Riesgo por Derrumbes?"),
        required = False
    )

    ## Riesgo por zona sísmica
    riesgo_zona_sismica = forms.BooleanField(
        label=_("¿Riesgo por Zona Sísmica?"),
        required = False
    )

    ## Animales que hay en la vivienda
    animales = forms.CharField(
        label = ('Animales que tiene:'),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-md','data-rule-required': 'true', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Indique los animales que tiene"),
        }),
        required=False
    )

    ## Estado donde se encuentra ubicada la vivienda
    estado = forms.CharField(
        label=_("Estado"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra el estado"),
            'readonly' : 'true',
            #'onchange': "actualizar_combo(this.value,'base','Municipio','estado','pk','nombre','id_municipio')"
        }), required=False
    )

    ## Municipio donde se encuentra ubicada la vivienda
    municipio = forms.CharField(
        label=_("Municipio"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra el municipio"),
            'readonly' : 'true',
            #'onchange': "actualizar_combo(this.value,'base','Parroquia','municipio','pk','nombre','id_parroquia')"
        }), required=False
    )

    ## Parroquia donde se encuentra ubicada la vivienda
    parroquia = forms.CharField(
        label=_("Parroquia"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm','data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra la parroquia"),
            'readonly' : 'true',
            #'onchange': "actualizar_combo(this.value,'base','ConsejoComunal','parroquia','pk','nombre','id_consejo_comunal')"
        }), required=False
    )

    ## Consejo comunal donde se encuentra ubicada la vivienda
    consejo_comunal = forms.CharField(
        label=_("Consejo Comunal"),
        widget=forms.TextInput(attrs={
            'class': 'form-control input-sm','data-toggle': 'tooltip', 'style':'width:250px;',
            'title': _("Muestra el consejo comunal"),
            'readonly':'true',
            #'onchange': "obtener_rif(this.value)",
        }), required=False
    )

    ## Rif del consejo comunal
    rif_consejo_comunal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm','data-toggle': 'tooltip', 'style':'width:100px;',
                'readonly':'true',
                'title': _("Muestra el RIF del Consejo Comunal"),
            }
        ), required=False
    )

    ## Dirección exacta de la vivienda
    direccion = forms.CharField(
        label=_("Dirección:"),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique la Dirección de la vivienda"),
            }
        )
    )

    ## Coordenadas geográficas de la vivienda
    coordenada = CoordenadaField()

    ## Alguna observación acerca de la vivienda
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
        """!
        Método que permite validar el formulario incluyendo todos los campos

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna el formulario con los rectpectivos errores
        """

        cleaned_data = super(ViviendaForm, self).clean()
        metro_cuadrado = float(self.cleaned_data['metro_cuadrado'])
        productivo = float(self.cleaned_data['productivo'])
        por_producir = float(self.cleaned_data['por_producir'])

        tipo_piso = self.cleaned_data['tipo_piso']
        tipo_cemento = self.cleaned_data['tipo_cemento']

        if metro_cuadrado < 0:
            msg = str(_("El valor de los metros cuadrados del terreno debe ser mayor a 0"))
            self.add_error('metro_cuadrado', msg)

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
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = Vivienda
        exclude = ['user','consejo_comunal']

class ViviendaUpdateForm(ViviendaForm):
    """!
    Clase que contiene los campos del formulario para actualizar los datos de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        super(ViviendaUpdateForm, self).__init__(*args, **kwargs)
        self.fields['fecha_hora'].required = False

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """

        model = Vivienda
        exclude = [
            'user','fecha_hora','consejo_comunal'
        ]

class ImagenForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de las imágenes de la vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        user = kwargs.pop('user')
        super(ImagenForm, self).__init__(*args, **kwargs)

        lista_vivienda = [('','Selecione...')]
        for vi in Vivienda.objects.filter(user=user):
            lista_vivienda.append( (vi.id,vi.numero_vivienda+"-"+str(vi.id)) )
        self.fields['vivienda'].choices = lista_vivienda

    ## Viviendas
    vivienda = forms.ChoiceField(
        label=_("Vivienda:"),
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Seleccione la Vivienda"),
            }
        )
    )

    ## Imágenes de la vivienda
    archivo_imagen = forms.ImageField()

    ## Imagen cifrada en base64
    imagen_base64 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'invisible',
            }
        ), required=False
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        """
        
        model = Imagen
        exclude = [
            'vivienda', 'nombre'
        ]
