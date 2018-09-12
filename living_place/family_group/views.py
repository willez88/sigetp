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
## @namespace family_group.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas de la aplicación grupo_familiar
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
from .models import FamilyGroup
from .forms import FamilyGroupForm
from living_place.models import LivingPlace
from django.contrib.auth.models import User
from user.models import CommunalCouncilLevel

# Create your views here.

class FamilyGroupListView(ListView):
    """!
    Clase que permite listar todos los grupos familiares

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = FamilyGroup
    template_name = 'family_group/list.html'

    def get_queryset(self):
        """!
        Método que obtiene la lista de grupos familiares que están asociados al usuario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la lista de objetos grupo familiar que pertenecen a la vivienda
        """

        if CommunalCouncilLevel.objects.filter(profile=self.request.user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=self.request.user.profile)
            queryset = FamilyGroup.objects.filter(living_place__communal_council=communal_council_level.communal_council)
            return queryset

        queryset = FamilyGroup.objects.filter(living_place__user=self.request.user)
        return queryset

class FamilyGroupCreateView(CreateView):
    """!
    Clase que permite registrar grupos familiares y asociarlos a las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = FamilyGroup
    form_class = FamilyGroupForm
    template_name = 'family_group/create.html'
    success_url = reverse_lazy('living_place:family_group:list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(FamilyGroupCreateView, self).get_form_kwargs()
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

        living_place = LivingPlace.objects.get(pk=form.cleaned_data['living_place'])
        self.object = form.save(commit=False)
        self.object.living_place = living_place
        self.object.family_last_name = form.cleaned_data['family_last_name']
        if form.cleaned_data['beneficiary_family']:
            self.object.beneficiary_family = form.cleaned_data['beneficiary_family']
        self.object.tenure = form.cleaned_data['tenure']
        if form.cleaned_data['tenure'] == 'AL':
            self.object.rented = form.cleaned_data['rented']
        if form.cleaned_data['ticket']:
            self.object.ticket= form.cleaned_data['ticket']
        self.object.observation = form.cleaned_data['observation']
        self.object.save()
        return super(FamilyGroupCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(FamilyGroupCreateView, self).form_invalid(form)

class FamilyGroupUpdateView(UpdateView):
    """!
    Clase que permite actualizar los datos del grupo familiar

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = FamilyGroup
    form_class = FamilyGroupForm
    template_name = 'family_group/create.html'
    success_url = reverse_lazy('living_place:family_group:list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(FamilyGroupUpdateView, self).get_form_kwargs()
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

        if CommunalCouncilLevel.objects.filter(profile=self.request.user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=self.request.user.profile)
            if FamilyGroup.objects.filter(pk=self.kwargs['pk'],living_place__communal_council=communal_council_level.communal_council):
                return super(FamilyGroupUpdateView, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if FamilyGroup.objects.filter(pk=self.kwargs['pk'],living_place__user=self.request.user):
            return super(FamilyGroupUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):
        """!
        Método que agrega valores predeterminados a los campos del formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        initial_data = super(FamilyGroupUpdateView, self).get_initial()
        initial_data['living_place'] = self.object.living_place.id
        return initial_data

class FamilyGroupDeleteView(DeleteView):
    """!
    Clase que permite borrar los datos de los grupos familiares

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = FamilyGroup
    template_name = 'family_group/delete.html'
    success_url = reverse_lazy('living_place:family_group:list')

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

        if CommunalCouncilLevel.objects.filter(profile=self.request.user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=self.request.user.profile)
            if FamilyGroup.objects.filter(pk=self.kwargs['pk'],living_place__communal_council=communal_council_level.communal_council):
                return super(FamilyGroupDeleteView, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if FamilyGroup.objects.filter(pk=self.kwargs['pk'],living_place__user=self.request.user):
            return super(FamilyGroupDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')