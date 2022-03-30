from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from living_place.models import LivingPlace
from user.models import CommunalCouncilLevel

from .forms import FamilyGroupForm
from .models import FamilyGroup


class FamilyGroupListView(ListView):
    """!
    Clase que permite listar todos los grupos familiares

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = FamilyGroup
    template_name = 'family_group/list.html'

    def get_queryset(self):
        """!
        Método que obtiene la lista de grupos familiares que están asociados al
        usuario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la lista de objetos grupo familiar que pertenecen a la
            vivienda
        """

        if CommunalCouncilLevel.objects.filter(
            profile=self.request.user.profile
        ):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=self.request.user.profile
            )
            ccl = communal_council_level.communal_council
            queryset = FamilyGroup.objects.filter(
                living_place__communal_council=ccl
            )
            return queryset

        queryset = FamilyGroup.objects.filter(
            living_place__user=self.request.user
        )
        return queryset


class FamilyGroupCreateView(CreateView):
    """!
    Clase que permite registrar grupos familiares y asociarlos a las viviendas

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = FamilyGroup
    form_class = FamilyGroupForm
    template_name = 'family_group/create.html'
    success_url = reverse_lazy('living_place:family_group:list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """!
        Método que valida si el formulario es correcto

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de
            registro
        @return Retorna el formulario validado
        """

        living_place = LivingPlace.objects.get(
            pk=form.cleaned_data['living_place']
        )
        self.object = form.save(commit=False)
        self.object.living_place = living_place
        self.object.family_last_name = form.cleaned_data['family_last_name']
        if form.cleaned_data['beneficiary_family']:
            self.object.beneficiary_family = form.cleaned_data[
                'beneficiary_family'
            ]
        self.object.tenure = form.cleaned_data['tenure']
        if form.cleaned_data['tenure'].id == 2:
            self.object.rented = form.cleaned_data['rented']
        if form.cleaned_data['ticket']:
            self.object.ticket = form.cleaned_data['ticket']
        self.object.observation = form.cleaned_data['observation']
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class FamilyGroupUpdateView(UpdateView):
    """!
    Clase que permite actualizar los datos del grupo familiar

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = FamilyGroup
    form_class = FamilyGroupForm
    template_name = 'family_group/create.html'
    success_url = reverse_lazy('living_place:family_group:list')

    def get_form_kwargs(self):
        """!
        Método que permite pasar el usuario actualmente logueado al formulario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con el usuario actualmente logueado
        """

        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar
        a esta vista

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos en
            caso de no ser el usuario logueado
        """

        if CommunalCouncilLevel.objects.filter(
            profile=self.request.user.profile
        ):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=self.request.user.profile
            )
            ccl = communal_council_level.communal_council
            if FamilyGroup.objects.filter(
                pk=self.kwargs['pk'],
                living_place__communal_council=ccl
            ):
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if FamilyGroup.objects.filter(
            pk=self.kwargs['pk'], living_place__user=self.request.user
        ):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_initial(self):
        """!
        Método que agrega valores predeterminados a los campos del formulario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        initial_data = super().get_initial()
        initial_data['living_place'] = self.object.living_place.id
        return initial_data


class FamilyGroupDeleteView(DeleteView):
    """!
    Clase que permite borrar los datos de los grupos familiares

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = FamilyGroup
    template_name = 'family_group/delete.html'
    success_url = reverse_lazy('living_place:family_group:list')

    def dispatch(self, request, *args, **kwargs):
        """!
        Metodo que valida si el usuario del sistema tiene permisos para entrar
        a esta vista

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param request <b>{object}</b> Objeto que contiene la petición
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param **kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        @return Redirecciona al usuario a la página de error de permisos en
            caso de no ser el usuario logueado
        """

        if CommunalCouncilLevel.objects.filter(
            profile=self.request.user.profile
        ):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=self.request.user.profile
            )
            ccl = communal_council_level.communal_council
            if FamilyGroup.objects.filter(
                pk=self.kwargs['pk'],
                living_place__communal_council=ccl
            ):
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if FamilyGroup.objects.filter(
            pk=self.kwargs['pk'], living_place__user=self.request.user
        ):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')
