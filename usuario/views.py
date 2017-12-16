from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .forms import PerfilUpdateForm
from .models import Perfil

# Create your views here.

class PerfilUpdate(UpdateView):
    model = User
    form_class = PerfilUpdateForm
    template_name = "usuario.actualizar.html"
    success_url = reverse_lazy('inicio')

    def dispatch(self, request, *args, **kwargs):
        if not int(self.request.user.pk) == int(self.kwargs['pk']):
            return redirect('base_403')
        return super(PerfilUpdate, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
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
