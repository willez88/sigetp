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
from django.views.generic import UpdateView, ListView, CreateView
from .forms import CommunalUpdateForm, PollsterForm, PollsterUpdateForm, PollsterStatusForm
from .models import Profile, Communal, Pollster
from django.conf import settings
from base.constant import EMAIL_SUBJECT
from base.functions import send_email
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.

class CommunalUpdateView(UpdateView):
    """!
    Clase que permite a un usuario registrado en el sistema actualizar sus datos de perfil

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    model = User
    form_class = CommunalUpdateForm
    template_name = 'usuario/profile.create.html'
    success_url = reverse_lazy('base:home')

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

        if int(self.request.user.pk) == int(self.kwargs['pk']) and self.request.user.profile.level == 1:
            return super(CommunalUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):
        """!
        Metodo que agrega valores predeterminados a los campos del formulario

        @author William Páez (wpaez at cenditel.gob.ve)
        @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
        @date 24-05-2017
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        initial_data = super(CommunalUpdateView, self).get_initial()
        initial_data['username'] = self.object.username
        initial_data['first_name'] = self.object.first_name
        initial_data['last_name'] = self.object.last_name
        initial_data['email'] = self.object.email
        communal = Communal.objects.get(profile=self.object.profile)
        initial_data['phone'] = communal.profile.phone
        initial_data['communal_council'] = communal.communal_council
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
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.save()

        profile = Profile.objects.get(user=self.object)

        if Profile.objects.filter(user=self.object):
            profile = Profile.objects.get(user=self.object)
            profile.phone = form.cleaned_data['phone']
            profile.save()

        return super(CommunalUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(CommunalUpdateView, self).form_invalid(form)

class PollsterListView(ListView):
    model = Pollster
    template_name = 'usuario/pollster.list.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.profile.level == 1:
            return super(PollsterListView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_queryset(self):
        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            queryset = Pollster.objects.filter(communal=communal)
            return queryset

class PollsterCreateView(CreateView):
    model = User
    form_class = PollsterForm
    template_name = 'usuario/profile.create.html'
    success_url = reverse_lazy('usuario:pollster_list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.profile.level == 1:
            return super(PollsterCreateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_form_kwargs(self):
        kwargs = super(PollsterCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.set_password(form.cleaned_data['password'])
        self.object.is_active = True
        self.object.save()

        profile = Profile.objects.create(
            phone=form.cleaned_data['phone'],
            level = 2,
            user= self.object
        )

        communal = Communal.objects.get(profile=self.request.user.profile)
        Pollster.objects.create(
            communal = communal,
            profile = profile
        )

        admin, admin_email = '', ''
        if settings.ADMINS:
            admin = settings.ADMINS[0][0]
            admin_email = settings.ADMINS[0][1]

        sent = send_email(self.object.email, 'usuario/welcome.mail', EMAIL_SUBJECT, {'first_name':self.request.user.first_name,
            'last_name':self.request.user.last_name, 'email':self.request.user.email, 'phone':self.request.user.profile.phone,
            'communal':communal, 'username':self.object.username, 'password':form.cleaned_data['password'],
            'admin':admin, 'admin_email':admin_email, 'emailapp':settings.EMAIL_FROM, 'url':get_current_site(self.request).name
        })

        return super(PollsterCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(PollsterCreateView, self).form_invalid(form)

class PollsterUpdateView(UpdateView):
    model = User
    form_class = PollsterUpdateForm
    template_name = 'usuario/profile.create.html'
    success_url = reverse_lazy('base:home')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id == self.kwargs['pk'] and self.request.user.profile.level == 2:
            return super(PollsterUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    """def get_form_kwargs(self):
        kwargs = super(PollsterUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs"""

    def get_initial(self):
        initial_data = super(PollsterUpdateView, self).get_initial()
        initial_data['username'] = self.object.username
        initial_data['first_name'] = self.object.first_name
        initial_data['last_name'] = self.object.last_name
        initial_data['email'] = self.object.email
        initial_data['phone'] = self.object.profile.phone
        if Pollster.objects.filter(profile=self.object.profile):
            pollster = Pollster.objects.get(profile=self.object.profile)
            initial_data['communal_council'] = pollster.communal.communal_council
        return initial_data

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.save()

        if Profile.objects.filter(user=self.object):
            profile = Profile.objects.get(user=self.object)
            profile.phone = form.cleaned_data['phone']
            profile.save()

        return super(PollsterUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(PollsterUpdateView, self).form_invalid(form)

class PollsterStatusUpdateView(UpdateView):

    model = User
    form_class = PollsterStatusForm
    template_name = 'usuario/pollster.status.update.html'
    success_url = reverse_lazy('usuario:pollster_list')

    def dispatch(self, request, *args, **kwargs):
        if Communal.objects.filter(profile=self.request.user.profile):
            communal = Communal.objects.get(profile=self.request.user.profile)
            pollster = Pollster.objects.filter(communal=communal,profile__user__pk=self.kwargs['pk'])
        if pollster and self.request.user.profile.level == 1:
            return super(PollsterStatusUpdateView, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):
        initial_data = super(PollsterStatusUpdateView, self).get_initial()
        initial_data['is_active'] = self.object.is_active
        return initial_data

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = form.cleaned_data['is_active']
        self.object.save()
        return super(PollsterStatusUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(PollsterStatusUpdateView, self).form_invalid(form)
