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
## @namespace living_place.views
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
from .models import LivingPlace, Photograph
from .forms import LivingPlaceForm, LivingPlaceUpdateForm, PhotographForm
from django.contrib.auth.models import User
from base.models import CommunalCouncil, Animal
from user.models import Profile, CommunalCouncilLevel, Pollster

# Create your views here.

class LivingPlaceListView(ListView):
    """!
    Clase que permite listar todas las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = LivingPlace
    template_name = 'living_place/list.html'

    def get_queryset(self):
        """!
        Método que obtiene la lista de viviendas que están asociadas al usuario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Lista de objetos vivienda que pertenecen al usuario
        """

        if CommunalCouncilLevel.objects.filter(profile=self.request.user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=self.request.user.profile)
            queryset = LivingPlace.objects.filter(communal_council=communal_council_level.communal_council)
            return queryset

        queryset = LivingPlace.objects.filter(user=self.request.user)
        return queryset

class LivingPlaceCreateView(CreateView):
    """!
    Clase que permite registrar viviendas y asociarlas al usuario

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = LivingPlace
    form_class = LivingPlaceForm
    template_name = 'living_place/create.html'
    success_url = reverse_lazy('living_place:list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(LivingPlaceCreateView, self).get_form_kwargs()
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
        self.object.date_time = form.cleaned_data['date_time']
        self.object.roof_type = form.cleaned_data['roof_type']
        self.object.electric_service = form.cleaned_data['electric_service']
        self.object.sanitary_situation = form.cleaned_data['sanitary_situation']
        self.object.trash_disposal = form.cleaned_data['trash_disposal']
        self.object.living_place_type = form.cleaned_data['living_place_type']
        self.object.wall_type = form.cleaned_data['wall_type']

        if form.cleaned_data['wall_type'] == 'BL':
            self.object.wall_frieze = form.cleaned_data['wall_frieze']

        self.object.floor_type = form.cleaned_data['floor_type']

        if form.cleaned_data['floor_type'] == 'CE':
            self.object.cement_type = form.cleaned_data['cement_type']

        self.object.living_place_condition = form.cleaned_data['living_place_condition']
        self.object.roof_condition = form.cleaned_data['roof_condition']
        self.object.wall_condition = form.cleaned_data['wall_condition']
        self.object.floor_condition = form.cleaned_data['floor_condition']
        self.object.ventilation_condition = form.cleaned_data['ventilation_condition']
        self.object.ilumination_condition = form.cleaned_data['ilumination_condition']
        self.object.ambulatory_accessibility = form.cleaned_data['ambulatory_accessibility']
        self.object.school_accessibility = form.cleaned_data['school_accessibility']
        self.object.lyceum_accessibility = form.cleaned_data['lyceum_accessibility']
        self.object.supply_center_accessibility = form.cleaned_data['supply_center_accessibility']
        self.object.rooms_number = form.cleaned_data['rooms_number']
        self.object.living_rooms_number = form.cleaned_data['living_rooms_number']
        self.object.bathrooms_number = form.cleaned_data['bathrooms_number']

        if form.cleaned_data['has_terrain']:
            self.object.has_terrain = form.cleaned_data['has_terrain']
            self.object.square_meter = form.cleaned_data['square_meter']
            self.object.productive = form.cleaned_data['productive']
            self.object.non_productive = form.cleaned_data['non_productive']

        if form.cleaned_data['river_risk']:
            self.object.river_risk = form.cleaned_data['river_risk']

        if form.cleaned_data['gully_risk']:
            self.object.gully_risk = form.cleaned_data['gully_risk']

        if form.cleaned_data['landslides_risk']:
            self.object.landslides_risk = form.cleaned_data['landslides_risk']

        if form.cleaned_data['seismic_zone_risk']:
            self.object.seismic_zone_risk = form.cleaned_data['seismic_zone_risk']

        #print(form.cleaned_data['animals'][0])
        #animal = Animal.objects.get(id=form.cleaned_data['animals'][0])
        #print(animal)
        #self.object.animals.add(animal)

        if CommunalCouncilLevel.objects.filter(profile=self.request.user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=self.request.user.profile)
            self.object.communal_council = communal_council_level.communal_council
        if Pollster.objects.filter(profile=self.request.user.profile):
            pollster = Pollster.objects.get(profile=self.request.user.profile)
            self.object.communal_council = pollster.communal_council_level.communal_council

        self.object.address = form.cleaned_data['address']
        self.object.living_place_number = form.cleaned_data['living_place_number']
        self.object.coordinates = form.cleaned_data['coordinate']
        self.object.observation = form.cleaned_data['observation']
        self.object.user = self.request.user
        self.object.save()
        #self.object.animals.add(animal)
        return super(LivingPlaceCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(LivingPlaceCreateView, self).form_invalid(form)

class LivingPlaceUpdateView(UpdateView):
    """!
    Clase que permite actualizar los datos de viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = LivingPlace
    form_class = LivingPlaceUpdateForm
    template_name = 'living_place/create.html'
    success_url = reverse_lazy('living_place:list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(LivingPlaceUpdateView, self).get_form_kwargs()
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
            if LivingPlace.objects.filter(pk=self.kwargs['pk'],communal_council=communal_council_level.communal_council):
                return super(LivingPlaceUpdateView, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if LivingPlace.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(LivingPlaceUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base_403')

    def get_context_data(self, **kwargs):
        context = super(LivingPlaceUpdateView, self).get_context_data(**kwargs)
        context['animal_list'] = self.object.animals.all()
        return context

    def get_initial(self):
        """!
        Método que agrega valores predeterminados a los campos del formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        initial_data = super(LivingPlaceUpdateView, self).get_initial()
        #vivienda = Vivienda.objects.get(pk=self.object.id)
        initial_data['date_time'] = self.object.date_time
        print(self.object.animals.all())
        initial_data['coordinate'] = self.object.coordinate.split(',')
        return initial_data

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
        self.object.coordinate = form.cleaned_data['coordinate']
        self.object.save()
        return super(LivingPlaceUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LivingPlaceUpdateView, self).form_invalid(form)

class LivingPlaceDeleteView(DeleteView):
    """!
    Clase que permite borrar los datos de las vivienda

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = LivingPlace
    template_name = 'living_place/delete.html'
    success_url = reverse_lazy('living_place:list')

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
            if LivingPlace.objects.filter(pk=self.kwargs['pk'],communal_council=communal_council_level.communal_council):
                return super(LivingPlaceDeleteView, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if LivingPlace.objects.filter(pk=self.kwargs['pk'],user=self.request.user):
            return super(LivingPlaceDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

class PhotographListView(ListView):
    """!
    Clase que permite listar todas las imágenes de las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Photograph
    template_name = 'living_place/photograph.list.html'

    def get_queryset(self):
        """!
        Método que obtiene la consulta según algún filtro especificado

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Lista de objetos imágenes que pertenecen al usuario
        """

        if CommunalCouncilLevel.objects.filter(profile=self.request.user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(profile=self.request.user.profile)
            queryset = Photograph.objects.filter(living_place__communal_council=communal_council_level.communal_council)
            return queryset

        queryset = Photograph.objects.filter(living_place__user=self.request.user)
        return queryset

class PhotographCreateView(CreateView):
    """!
    Clase que permite registrar imágenes y asociarlas a las viviendas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Photograph
    form_class = PhotographForm
    template_name = 'living_place/photograph.create.html'
    success_url = reverse_lazy('living_place:photograph_list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar valores de la vista al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna los datos en un diccionario
        """

        kwargs = super(PhotographCreateView, self).get_form_kwargs()
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
        self.object.name = form.cleaned_data['picture']
        living_place = LivingPlace.objects.get(pk=form.cleaned_data['living_place'])
        self.object.living_place = living_place
        self.object.picture = form.cleaned_data['picture']
        self.object.save()
        return super(PhotographCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(PhotographCreateView, self).form_invalid(form)

class PhotographDeleteView(DeleteView):
    """!
    Clase que permite eliminar los datos de las imágenes

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Photograph
    template_name = 'living_place/photograph.delete.html'
    success_url = reverse_lazy('living_place:photograph_delete')

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
            if Photograph.objects.filter(pk=self.kwargs['pk'],living_place__communal_council=communal_council_level.communal_council):
                return super(PhotographDeleteView, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Photograph.objects.filter(pk=self.kwargs['pk'],living_place__user=self.request.user):
            return super(PhotographDeleteView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')
