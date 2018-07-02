"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CIDA (2017)

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
## @namespace vivienda.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas de la aplicación vivienda
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vivienda, Imagen
from .forms import ViviendaForm, ViviendaUpdateForm, ImagenForm
from django.contrib.auth.models import User
from base.models import CommunalCouncil
from usuario.models import Profile, Pollster, Communal

# Create your views here.

class ViviendaList(ListView):
    """!
    Clase que permite listar todas las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Vivienda
    template_name = 'vivienda.lista.html'

    def get_queryset(self):
        """!
        Método que obtiene la lista de viviendas que están asociadas al usuario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la lista de objetos vivienda que pertenecen al usuario
        """

        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            queryset = Vivienda.objects.filter(communal_council=communal.communal_council)
            return queryset

        queryset = Vivienda.objects.filter(user=self.request.user)
        return queryset

class ViviendaCreate(CreateView):
    """!
    Clase que permite registrar viviendas y asociarlas al usuario

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Vivienda
    form_class = ViviendaForm
    template_name = 'vivienda.registro.html'
    success_url = reverse_lazy('vivienda_lista')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(ViviendaCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """!
        Método que valida si el formulario es correcto

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de registro
        @return Retorna el formulario validado
        """

        self.object = form.save(commit=False)
        self.object.fecha_hora = form.cleaned_data['fecha_hora']
        self.object.tipo_techo = form.cleaned_data['tipo_techo']
        self.object.servicio_electrico = form.cleaned_data['servicio_electrico']
        self.object.situacion_sanitaria = form.cleaned_data['situacion_sanitaria']
        self.object.disposicion_basura = form.cleaned_data['disposicion_basura']
        self.object.tipo_vivienda = form.cleaned_data['tipo_vivienda']
        self.object.tipo_pared = form.cleaned_data['tipo_pared']

        if form.cleaned_data['tipo_pared'] == 'BL':
            self.object.pared_frizada = form.cleaned_data['pared_frizada']

        self.object.tipo_piso = form.cleaned_data['tipo_piso']

        if form.cleaned_data['tipo_piso'] == 'CE':
            self.object.tipo_cemento = form.cleaned_data['tipo_cemento']

        self.object.condicion_vivienda = form.cleaned_data['condicion_vivienda']
        self.object.condicion_techo = form.cleaned_data['condicion_techo']
        self.object.condicion_pared = form.cleaned_data['condicion_pared']
        self.object.condicion_piso = form.cleaned_data['condicion_piso']
        self.object.condicion_ventilacion = form.cleaned_data['condicion_ventilacion']
        self.object.condicion_iluminacion = form.cleaned_data['condicion_iluminacion']
        self.object.accesibilidad_ambulatorio = form.cleaned_data['accesibilidad_ambulatorio']
        self.object.accesibilidad_escuela = form.cleaned_data['accesibilidad_escuela']
        self.object.accesibilidad_liceo = form.cleaned_data['accesibilidad_liceo']
        self.object.accesibilidad_centro_abastecimiento = form.cleaned_data['accesibilidad_centro_abastecimiento']
        self.object.numero_habitaciones = form.cleaned_data['numero_habitaciones']
        self.object.numero_salas = form.cleaned_data['numero_salas']
        self.object.numero_banhos = form.cleaned_data['numero_banhos']

        if form.cleaned_data['tiene_terreno']:
            self.object.tiene_terreno = form.cleaned_data['tiene_terreno']
            self.object.metro_cuadrado = form.cleaned_data['metro_cuadrado']
            self.object.productivo = form.cleaned_data['productivo']
            self.object.por_producir = form.cleaned_data['por_producir']

        if form.cleaned_data['riesgo_rio']:
            self.object.riesgo_rio = form.cleaned_data['riesgo_rio']

        if form.cleaned_data['riesgo_quebrada']:
            self.object.riesgo_quebrada = form.cleaned_data['riesgo_quebrada']

        if form.cleaned_data['riesgo_derrumbe']:
            self.object.riesgo_derrumbe = form.cleaned_data['riesgo_derrumbe']

        if form.cleaned_data['riesgo_zona_sismica']:
            self.object.riesgo_zona_sismisca = form.cleaned_data['riesgo_zona_sismica']

        self.object.animales = form.cleaned_data['animales']

        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            self.object.communal_council = communal.communal_council
        if Pollster.objects.filter(profile=self.request.user.profile):
            pollster = Pollster.objects.get(profile=self.request.user.profile)
            self.object.communal_council = pollster.communal.communal_council

        self.object.direccion = form.cleaned_data['direccion']
        self.object.numero_vivienda = form.cleaned_data['numero_vivienda']
        self.object.coordenadas = form.cleaned_data['coordenada']
        self.object.observacion = form.cleaned_data['observacion']

        """if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            self.object.user = communal.profile.user
        if Pollster.objects.filter(profile=self.request.user.profile):
            pollster = Pollster.objects.get(profile=self.request.user.profile)
            self.object.user = pollster.profile.user"""
        self.object.user = self.request.user
        self.object.save()
        return super(ViviendaCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ViviendaCreate, self).form_invalid(form)

class ViviendaUpdate(UpdateView):
    """!
    Clase que permite actualizar los datos de viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Vivienda
    form_class = ViviendaUpdateForm
    template_name = 'vivienda.registro.html'
    success_url = reverse_lazy('vivienda_lista')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(ViviendaUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar a esta vista

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos en caso
                de no ser el usuario logueado
        """

        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            if Vivienda.objects.filter(pk=self.kwargs['pk'],communal_council=communal.communal_council):
                return super(ViviendaUpdate, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Vivienda.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(ViviendaUpdate, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base_403')

    def get_initial(self):
        """!
        Método que agrega valores predeterminados a los campos del formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        datos_iniciales = super(ViviendaUpdate, self).get_initial()
        vivienda = Vivienda.objects.get(pk=self.object.id)
        datos_iniciales['fecha_hora'] = vivienda.fecha_hora
        datos_iniciales['coordenada'] = vivienda.coordenadas.split(",")
        return datos_iniciales

    def form_valid(self, form):
        """!
        Metodo que valida si el formulario es correcto

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de registro
        @return Retorna el formulario validado
        """

        self.object = form.save(commit=False)
        self.object.coordenadas = form.cleaned_data['coordenada']
        self.object.save()
        return super(ViviendaUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(ViviendaUpdate, self).form_invalid(form)

class ViviendaDelete(DeleteView):
    """!
    Clase que permite borrar los datos de las vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Vivienda
    template_name = 'vivienda.eliminar.html'
    success_url = reverse_lazy('vivienda_lista')

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar a esta vista

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos en caso
                de no ser el usuario logueado
        """

        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            if Vivienda.objects.filter(pk=self.kwargs['pk'],communal_council=communal.communal_council):
                return super(ViviendaDelete, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Vivienda.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(ViviendaDelete, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

class ImagenList(ListView):
    """!
    Clase que permite listar todas las imágenes de las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Imagen
    template_name = "imagen.lista.html"

    def get_queryset(self):
        """!
        Método que obtiene la consulta según algún filtro especificado

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la lista de objetos imágenes que pertenecen al usuario
        """

        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            queryset = Imagen.objects.filter(vivienda__communal_council=communal.communal_council)
            return queryset

        queryset = Imagen.objects.filter(vivienda__user=self.request.user)
        return queryset

class ImagenCreate(CreateView):
    """!
    Clase que permite registrar imágenes y asociarlas a las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Imagen
    form_class = ImagenForm
    template_name = 'imagen.registro.html'
    success_url = reverse_lazy('imagen_lista')

    def get_form_kwargs(self):
        """!
        Método que permite pasar valores de la vista al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna los datos en un diccionario
        """

        kwargs = super(ImagenCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """!
        Metodo que valida si el formulario es correcto

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de registro
        @return Retorna el formulario validado
        """

        #print(form.cleaned_data['archivo_imagen'])
        self.object = form.save(commit=False)
        self.object.nombre = form.cleaned_data['archivo_imagen']
        vivienda = Vivienda.objects.get(pk=form.cleaned_data['vivienda'])
        self.object.vivienda = vivienda
        self.object.imagen_base64 = form.cleaned_data['imagen_base64']
        self.object.save()
        return super(ImagenCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(ImagenCreate, self).form_invalid(form)

class ImagenDelete(DeleteView):
    """!
    Clase que permite eliminar los datos de las imágenes

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Imagen
    template_name = 'imagen.eliminar.html'
    success_url = reverse_lazy('imagen_lista')

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar a esta vista

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos en caso
                de no ser el usuario logueado
        """

        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            if Imagen.objects.filter(pk=self.kwargs['pk'],vivienda__communal_council=communal.communal_council):
                return super(ImagenDelete, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Imagen.objects.filter(pk=self.kwargs['pk'],vivienda__user=self.request.user):
            return super(ImagenDelete, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')
