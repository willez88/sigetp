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
## @namespace grupo_familiar.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas de la aplicación grupo_familiar
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import GrupoFamiliar
from .forms import GrupoFamiliarForm
from vivienda.models import Vivienda
from django.contrib.auth.models import User

# Create your views here.

class GrupoFamiliarList(ListView):
    """!
    Clase que permite listar todos los grupos familiares

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = GrupoFamiliar
    template_name = "grupo.familiar.lista.html"

    def get_queryset(self):
        """!
        Método que obtiene la lista de grupos familiares que están asociados al usuario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la lista de objetos grupo familiar que pertenecen a la vivienda
        """

        queryset = GrupoFamiliar.objects.filter(vivienda__user=self.request.user)
        return queryset

class GrupoFamiliarCreate(CreateView):
    """!
    Clase que permite registrar grupos familiares y asociarlos a las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = GrupoFamiliar
    form_class = GrupoFamiliarForm
    template_name = "grupo.familiar.registro.html"
    success_url = reverse_lazy('grupo_familiar_lista')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(GrupoFamiliarCreate, self).get_form_kwargs()
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

        vivienda = Vivienda.objects.get(pk=form.cleaned_data['vivienda'])
        self.object = form.save(commit=False)
        self.object.vivienda = vivienda
        self.object.apellido_familia = form.cleaned_data['apellido_familia']
        if form.cleaned_data['familia_beneficiada']:
            self.object.familia_beneficiada = form.cleaned_data['familia_beneficiada']
        self.object.tenencia = form.cleaned_data['tenencia']
        if form.cleaned_data['tenencia'] == 'AL':
            self.object.alquilada = form.cleaned_data['alquilada']
        if form.cleaned_data['pasaje']:
            self.object.pasaje = form.cleaned_data['pasaje']
        self.object.observacion = form.cleaned_data['observacion']
        self.object.save()
        return super(GrupoFamiliarCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(GrupoFamiliarCreate, self).form_invalid(form)

class GrupoFamiliarUpdate(UpdateView):
    """!
    Clase que permite actualizar los datos del grupo familiar

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = GrupoFamiliar
    form_class = GrupoFamiliarForm
    template_name = "grupo.familiar.registro.html"
    success_url = reverse_lazy('grupo_familiar_lista')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(GrupoFamiliarUpdate, self).get_form_kwargs()
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

        user = User.objects.get(username=self.request.user.username)
        if not GrupoFamiliar.objects.filter(pk=self.kwargs['pk'],vivienda__user=user):
            return redirect('base_403')
        return super(GrupoFamiliarUpdate, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        """!
        Método que agrega valores predeterminados a los campos del formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        datos_iniciales = super(GrupoFamiliarUpdate, self).get_initial()
        grupo_familiar = GrupoFamiliar.objects.get(pk=self.object.id)
        datos_iniciales['vivienda'] = grupo_familiar.vivienda.id
        return datos_iniciales

class GrupoFamiliarDelete(DeleteView):
    """!
    Clase que permite borrar los datos de los grupos familiares

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = GrupoFamiliar
    template_name = "grupo.familiar.eliminar.html"
    success_url = reverse_lazy('grupo_familiar_lista')

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

        user = User.objects.get(username=self.request.user.username)
        if not GrupoFamiliar.objects.filter(pk=self.kwargs['pk'],vivienda__user=user):
            return redirect('base_403')
        return super(GrupoFamiliarDelete, self).dispatch(request, *args, **kwargs)
