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
## @namespace usuario.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas de la aplicación usuario
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .forms import PerfilUpdateForm
from .models import Perfil

# Create your views here.

class PerfilUpdate(UpdateView):
    """!
    Clase que permite a un usuario registrado en el sistema actualizar sus datos de perfil

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = User
    form_class = PerfilUpdateForm
    template_name = "usuario.actualizar.html"
    success_url = reverse_lazy('inicio')

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
        @return Redirecciona al usuario a la página de error de permisos si no es su perfil
        """

        if not int(self.request.user.pk) == int(self.kwargs['pk']):
            return redirect('base_403')
        return super(PerfilUpdate, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        """!
        Metodo que agrega valores predeterminados a los campos del formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        datos_iniciales = super(PerfilUpdate, self).get_initial()
        #user = User.objects.get(pk=self.request.user.pk)
        datos_iniciales['username'] = self.object.username
        datos_iniciales['nombre'] = self.object.first_name
        datos_iniciales['apellido'] = self.object.last_name
        datos_iniciales['correo'] = self.object.email
        perfil = Perfil.objects.get(user=self.object)
        datos_iniciales['cedula'] = perfil.cedula
        datos_iniciales['telefono'] = perfil.telefono
        datos_iniciales['consejo_comunal_temp'] = perfil.consejo_comunal
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
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['nombre']
        self.object.last_name = form.cleaned_data['apellido']
        self.object.email = form.cleaned_data['correo']
        self.object.save()

        perfil = Perfil.objects.get(user=self.object)

        ## Forma alternativa
        """Perfil.objects.update_or_create(
            pk=perfil.pk, defaults={
                'cedula': form.cleaned_data['cedula'],
                'telefono': form.cleaned_data['telefono'],
            }
        )"""

        if Perfil.objects.filter(user__username=str(self.object.username)):
            perfil = Perfil.objects.get(user__username=str(self.object.username))
            perfil.cedula = form.cleaned_data['cedula']
            perfil.telefono = form.cleaned_data['telefono']
            perfil.save()

        return super(PerfilUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(PerfilUpdate, self).form_invalid(form)
