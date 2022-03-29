from base.constant import EMAIL_SUBJECT
from base.functions import send_email
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView

from .forms import (
    CommunalCouncilLevelUpdateForm, PollsterForm, PollsterUpdateForm,
)
from .models import CommunalCouncilLevel, Pollster, Profile


class CommunalCouncilLevelUpdateView(UpdateView):
    """!
    Clase que permite a un usuario registrado en el sistema actualizar sus
    datos de perfil

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = Profile
    form_class = CommunalCouncilLevelUpdateForm
    template_name = 'user/profile.create.html'
    success_url = reverse_lazy('base:home')

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar
        a esta vista

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos si no
            es su perfil
        """

        if int(self.request.user.profile.pk) == int(self.kwargs['pk']) and\
                self.request.user.groups.get(name='Nivel Consejo Comunal'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):
        """!
        Metodo que agrega valores predeterminados a los campos del formulario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        initial_data = super().get_initial()
        initial_data['username'] = self.object.user.username
        initial_data['first_name'] = self.object.user.first_name
        initial_data['last_name'] = self.object.user.last_name
        initial_data['email'] = self.object.user.email
        communal_council_level = CommunalCouncilLevel.objects.get(
            profile=self.object
        )
        initial_data[
            'communal_council'
        ] = communal_council_level.communal_council
        return initial_data

    def form_valid(self, form):
        """!
        Metodo que valida si el formulario es correcto

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de
            registro
        @return Retorna el formulario validado
        """

        self.object = form.save()
        self.object.phone = form.cleaned_data['phone']
        self.object.save()
        user = User.objects.get(username=self.object.user.username)
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class PollsterListView(ListView):
    model = Pollster
    template_name = 'user/pollster.list.html'
    success_url = reverse_lazy('user:pollster_list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.groups.get(name='Nivel Consejo Comunal'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_queryset(self):
        if CommunalCouncilLevel.objects.filter(
            profile=self.request.user.profile
        ):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=self.request.user.profile
            )
            queryset = Pollster.objects.filter(
                communal_council_level=communal_council_level
            )
            return queryset

    def post(self, *args, **kwargs):
        '''
        Cambia el estado activo a el usuario
        @return: Dirige a la tabla que muestra los usuarios de la apliacion
        '''

        activate = self.request.POST.get('activate', None)
        deactivate = self.request.POST.get('deactivate', None)
        status = False

        if activate is not None:
            user = activate
            status = True
        elif deactivate is not None:
            user = deactivate
            status = False
        else:
            messages.error(
                self.request, 'Esta intentando hacer una accion incorrecta'
            )
        try:
            user = User.objects.get(pk=user)
            user.is_active = status
            user.save()
            if status:
                messages.success(
                    self.request,
                    'Se ha activado el usuario: %s' % (str(user))
                )
            else:
                messages.warning(
                    self.request,
                    'Se ha inactivado el usuario: %s' % (str(user))
                )
        except Exception as e:
            messages.info(self.request, e)
        return redirect(self.success_url)


class PollsterFormView(FormView):
    model = User
    form_class = PollsterForm
    template_name = 'user/profile.create.html'
    success_url = reverse_lazy('user:pollster_list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.groups.get(name='Nivel Consejo Comunal'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_form_kwargs(self):
        kwargs = super(PollsterFormView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.set_password(form.cleaned_data['password'])
        self.object.is_active = True
        self.object.groups.add(Group.objects.get(name='Nivel Encuestador'))
        self.object.save()

        profile = Profile.objects.create(
            phone=form.cleaned_data['phone'],
            user=self.object
        )

        communal_council_level = CommunalCouncilLevel.objects.get(
            profile=self.request.user.profile
        )
        Pollster.objects.create(
            communal_council_level=communal_council_level,
            profile=profile
        )

        admin, admin_email = '', ''
        if settings.ADMINS:
            admin = settings.ADMINS[0][0]
            admin_email = settings.ADMINS[0][1]

        send_email(
            self.object.email, 'user/welcome.mail', EMAIL_SUBJECT,
            {
                'first_name': self.request.user.first_name,
                'last_name': self.request.user.last_name,
                'email': self.request.user.email,
                'phone': self.request.user.profile.phone,
                'communal_council_level': communal_council_level,
                'username': self.object.username,
                'password': form.cleaned_data['password'],
                'admin': admin, 'admin_email': admin_email,
                'emailapp': settings.EMAIL_FROM,
                'url': get_current_site(self.request).name
            }
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class PollsterUpdateView(UpdateView):
    model = Profile
    form_class = PollsterUpdateForm
    template_name = 'user/profile.create.html'
    success_url = reverse_lazy('base:home')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.profile.pk == self.kwargs['pk'] and\
                self.request.user.groups.get(name='Nivel Encuestador'):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):
        initial_data = super(PollsterUpdateView, self).get_initial()
        initial_data['username'] = self.object.user.username
        initial_data['first_name'] = self.object.user.first_name
        initial_data['last_name'] = self.object.user.last_name
        initial_data['email'] = self.object.user.email
        if Pollster.objects.filter(profile=self.object):
            pollster = Pollster.objects.get(profile=self.object)
            initial_data[
                'communal_council'
            ] = pollster.communal_council_level.communal_council
        return initial_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.username = form.cleaned_data['username']
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.save()
        user = User.objects.get(username=self.object.user.username)
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
