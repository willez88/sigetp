from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .forms import PerfilUpdateForm
from .models import Perfil

# Create your views here.

class PerfilUpdate(UpdateView):
    model = Perfil
    form_class = PerfilUpdateForm
    template_name = "usuario.actualizar.html"
    success_url = reverse_lazy('inicio')

    def get_initial(self):
        datos_iniciales = super(PerfilUpdate, self).get_initial()
        datos_iniciales['username'] = self.object.user.username
        datos_iniciales['nombre'] = self.object.user.first_name
        datos_iniciales['apellido'] = self.object.user.last_name
        datos_iniciales['correo'] = self.object.user.email
        datos_iniciales['cedula'] = self.object.cedula
        datos_iniciales['telefono'] = self.object.telefono
        datos_iniciales['consejo_comunal_temp'] = self.object.consejo_comunal
        return datos_iniciales

    def form_valid(self, form):

        if User.objects.filter(pk=self.object.user.id):
            user = User.objects.get(pk=self.object.user.id)
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['nombre']
            user.last_name = form.cleaned_data['apellido']
            user.email = form.cleaned_data['correo']
            user.save()

        self.object = form.save(commit=False)
        self.object.cedula = form.cleaned_data['cedula']
        self.object.telefono = form.cleaned_data['telefono']
        self.object.save()

        return super(PerfilUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(PerfilUpdate, self).form_invalid(form)
