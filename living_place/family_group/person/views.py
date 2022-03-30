from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, ListView, TemplateView, UpdateView,
)
from living_place.family_group.models import FamilyGroup
from user.models import CommunalCouncilLevel

from .forms import PersonForm
from .models import Person


class PersonListView(ListView):
    """!
    Clase que permite listar todas las personas

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = Person
    template_name = 'person/list.html'

    def get_queryset(self):
        """!
        Método que obtiene la lista de personas que están asociadas al usuario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna la lista de objetos persona que pertenecen al
            grupo familiar
        """

        if CommunalCouncilLevel.objects.filter(
            profile=self.request.user.profile
        ):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=self.request.user.profile
            )
            ccl = communal_council_level.communal_council
            queryset = Person.objects.filter(
                family_group__living_place__communal_council=ccl
            )
            return queryset

        queryset = Person.objects.filter(
            family_group__living_place__user=self.request.user
        )
        return queryset


class PersonCreateView(CreateView):
    """!
    Clase que permite registrar personas y asociarlos a los grupos familiares

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = Person
    form_class = PersonForm
    template_name = 'person/create.html'
    success_url = reverse_lazy('living_place:family_group:person:list')

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

        family_group = FamilyGroup.objects.get(
            pk=form.cleaned_data['family_group']
        )
        self.object = form.save(commit=False)
        self.object.family_group = family_group
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        if form.cleaned_data['has_identity_card'] == 'S':
            self.object.identity_card = form.cleaned_data['identity_card']
        else:
            self.object.identity_card = None
        self.object.phone = form.cleaned_data['phone']
        self.object.email = form.cleaned_data['email']
        self.object.sex = form.cleaned_data['sex']
        self.object.birthdate = form.cleaned_data['birthdate']
        self.object.family_relationship = form.cleaned_data[
            'family_relationship'
        ]
        if form.cleaned_data['family_head']:
            self.object.family_head = form.cleaned_data['family_head']
        self.object.marital_status = form.cleaned_data['marital_status']
        self.object.instruction_degree = form.cleaned_data[
            'instruction_degree'
        ]
        self.object.educational_mission = form.cleaned_data[
            'educational_mission'
        ]
        self.object.profession = form.cleaned_data['profession']
        self.object.occupation = form.cleaned_data['occupation']
        self.object.workplace = form.cleaned_data['workplace']
        if form.cleaned_data['pensioner']:
            self.object.pensioner = form.cleaned_data['pensioner']
        if form.cleaned_data['retired']:
            self.object.retired = form.cleaned_data['retired']
        self.object.income_type = form.cleaned_data['income_type']
        # self.object.sport = form.cleaned_data['sport']
        # self.object.disease = form.cleaned_data['disease']
        # self.object.disability = form.cleaned_data['disability']
        if form.cleaned_data['communal_council_law']:
            self.object.communal_council_law = form.cleaned_data[
                'communal_council_law'
            ]
        # self.object.course = form.cleaned_data['course']
        # self.object.community_organization = form.cleaned_data[
        #    'community_organization'
        # ]
        self.object.leisure = form.cleaned_data['leisure']
        self.object.communication = form.cleaned_data['communication']
        self.object.insecurity = form.cleaned_data['insecurity']
        self.object.commentary = form.cleaned_data['commentary']
        self.object.observation = form.cleaned_data['observation']
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class PersonUpdateView(UpdateView):
    """!
    Clase que permite actualizar los datos de las personas

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = Person
    form_class = PersonForm
    template_name = 'person/create.html'
    success_url = reverse_lazy('living_place:family_group:person:list')

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
            if Person.objects.filter(
                pk=self.kwargs['pk'],
                family_group__living_place__communal_council=ccl
            ):
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Person.objects.filter(
            pk=self.kwargs['pk'],
            family_group__living_place__user=self.request.user
        ):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sports_list'] = self.object.sports.all()
        context['diseases_list'] = self.object.diseases.all()
        context['disabilities_list'] = self.object.disabilities.all()
        context['courses_list'] = self.object.courses.all()
        context[
            'community_organizations_list'
        ] = self.object.community_organizations.all()
        return context

    def get_initial(self):
        """!
        Método que agrega valores predeterminados a los campos del formulario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @return Retorna un diccionario con los valores predeterminados
        """

        initial_data = super(PersonUpdateView, self).get_initial()
        initial_data['family_group'] = self.object.family_group.id
        initial_data['age'] = self.object.age
        return initial_data

    def form_valid(self, form):
        """!
        Método que valida si el formulario es correcto

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param form <b>{object}</b> Objeto que contiene el formulario de
            registro
        @return Retorna el formulario validado
        """

        self.object = form.save(commit=False)
        if form.cleaned_data['has_identity_card'] == 'S':
            self.object.identity_card = form.cleaned_data['identity_card']
        else:
            self.object.identity_card = None
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class PersonDeleteView(DeleteView):
    """!
    Clase que permite borrar los datos de las personas

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    model = Person
    template_name = 'person/delete.html'
    success_url = reverse_lazy('living_place:family_group:person:list')

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
            if Person.objects.filter(
                pk=self.kwargs['pk'],
                family_group__living_place__communal_council=ccl
            ):
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('base:error_403')

        if Person.objects.filter(
            pk=self.kwargs['pk'],
            family_group__living_place__user=self.request.user
        ):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('base:error_403')


class PersonReportTemplateView(TemplateView):
    """!
    Clase que permite hacer un reporte

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    template_name = 'person/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        communal_council_level = CommunalCouncilLevel.objects.get(
            profile=self.request.user.profile
        )
        ccl = communal_council_level.communal_council
        context['communal_council_level'] = communal_council_level
        if Person.objects.filter(
            family_group__living_place__communal_council=ccl
        ):
            person = Person.objects.filter(
                family_group__living_place__communal_council=ccl
            )
            people = person.count()
            men = person.filter(gender__id=1).count()
            women = person.filter(gender__id=2).count()
            # print(people)
            # print(men)
            # print(women)
            percentage_men = (men/people)*100
            percentage_women = (women/people)*100
            # print(percentage_men)
            # print(percentage_women)
            context['person'] = person
            context['people'] = people
            context['men'] = men
            context['women'] = women
            context['percentage_men'] = '{0:.2f}'.format(percentage_men)
            context['percentage_women'] = '{0:.2f}'.format(percentage_women)
        return context
