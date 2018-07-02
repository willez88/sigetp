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
## @namespace persona.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas de la aplicación persona
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Persona
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PersonaForm
from vivienda.grupo_familiar.models import GrupoFamiliar
from django.contrib.auth.models import User
from usuario.models import Communal
import datetime

# Create your views here.

class PersonaList(ListView):
    """!
    Clase que permite listar todas las personas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Persona
    template_name = "persona.lista.html"

    def get_queryset(self):
        """!
        Método que obtiene la lista de personas que están asociadas al usuario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la lista de objetos persona que pertenecen al grupo familiar
        """

        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            queryset = Persona.objects.filter(grupo_familiar__vivienda__communal_council=communal.communal_council)
            return queryset

        queryset = Persona.objects.filter(grupo_familiar__vivienda__user=self.request.user)
        return queryset

class PersonaCreate(CreateView):
    """!
    Clase que permite registrar personas y asociarlos a los grupos familiares

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Persona
    form_class = PersonaForm
    template_name = "persona.registro.html"
    success_url = reverse_lazy('persona_lista')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(PersonaCreate, self).get_form_kwargs()
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

        grupo_familiar = GrupoFamiliar.objects.get(pk=form.cleaned_data['grupo_familiar'])
        self.object = form.save(commit=False)
        self.object.grupo_familiar = grupo_familiar
        self.object.nombre = form.cleaned_data['nombre']
        self.object.apellido = form.cleaned_data['apellido']
        if form.cleaned_data['tiene_cedula']=="S":
            self.object.cedula = form.cleaned_data['cedula']
        else:
            self.object.cedula = None
        self.object.telefono = form.cleaned_data['telefono']
        self.object.correo = form.cleaned_data['correo']
        self.object.sexo = form.cleaned_data['sexo']
        self.object.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        self.object.parentesco = form.cleaned_data['parentesco']
        if form.cleaned_data['jefe_familiar']:
            self.object.jefe_familiar = form.cleaned_data['jefe_familiar']
        self.object.estado_civil = form.cleaned_data['estado_civil']
        self.object.grado_instruccion = form.cleaned_data['grado_instruccion']
        self.object.mision_educativa = form.cleaned_data['mision_educativa']
        self.object.profesion = form.cleaned_data['profesion']
        self.object.ocupacion = form.cleaned_data['ocupacion']
        self.object.lugar_trabajo = form.cleaned_data['lugar_trabajo']
        if form.cleaned_data['jubilado']:
            self.object.jubilado = form.cleaned_data['jubilado']
        if form.cleaned_data['pensionado']:
            self.object.pensionado = form.cleaned_data['pensionado']
        self.object.ingreso = form.cleaned_data['ingreso']
        self.object.deporte = form.cleaned_data['deporte']
        self.object.enfermedad = form.cleaned_data['enfermedad']
        self.object.discapacidad = form.cleaned_data['discapacidad']
        if form.cleaned_data['ley_consejo_comunal']:
            self.object.ley_consejo_comunal = form.cleaned_data['ley_consejo_comunal']
        self.object.curso = form.cleaned_data['curso']
        self.object.organizacion_comunitaria = form.cleaned_data['organizacion_comunitaria']
        self.object.ocio = form.cleaned_data['ocio']
        self.object.mejorar_comunicacion = form.cleaned_data['mejorar_comunicacion']
        self.object.inseguridad = form.cleaned_data['inseguridad']
        self.object.comentario = form.cleaned_data['comentario']
        self.object.observacion = form.cleaned_data['observacion']
        self.object.save()
        return super(PersonaCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(PersonaCreate, self).form_invalid(form)

class PersonaUpdate(UpdateView):
    """!
    Clase que permite actualizar los datos de las personas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Persona
    form_class = PersonaForm
    template_name = "persona.registro.html"
    success_url = reverse_lazy('persona_lista')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super(PersonaUpdate, self).get_form_kwargs()
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
            if Persona.objects.filter(pk=self.kwargs['pk'],grupo_familiar__vivienda__communal_council=communal.communal_council):
                return super(PersonaUpdate, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Persona.objects.filter(pk=self.kwargs['pk'],vivienda__grupo_familiar__vivienda__user=user):
            return super(PersonaUpdate, self).dispatch(request, *args, **kwargs)
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

        datos_iniciales = super(PersonaUpdate, self).get_initial()
        datos_iniciales['grupo_familiar'] = self.object.grupo_familiar.id
        datos_iniciales['edad'] = self.object.edad
        return datos_iniciales

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
        if form.cleaned_data['tiene_cedula']=="S":
            self.object.cedula = form.cleaned_data['cedula']
        else:
            self.object.cedula = None
        self.object.save()
        return super(PersonaUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(PersonaUpdate, self).form_invalid(form)

class PersonaDelete(DeleteView):
    """!
    Clase que permite borrar los datos de las personas

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = Persona
    template_name = "persona.eliminar.html"
    success_url = reverse_lazy('persona_lista')

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
            if Persona.objects.filter(pk=self.kwargs['pk'],grupo_familiar__vivienda__communal_council=communal.communal_council):
                return super(PersonaDelete, self).dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Persona.objects.filter(pk=self.kwargs['pk'],grupo_familiar__vivienda__user=user):
            return super(PersonaDelete, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')
