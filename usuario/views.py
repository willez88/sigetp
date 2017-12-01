from django.shortcuts import render, redirect
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

    def dispatch(self, request, *args, **kwargs):
        if not int(self.request.user.pk) == int(self.kwargs['pk']):
            return redirect('base_403')
        return super(PerfilUpdate, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        datos_iniciales = super(PerfilUpdate, self).get_initial()
        user = User.objects.get(pk=self.request.user.pk)
        print(user.first_name)
        datos_iniciales['username'] = user.username
        datos_iniciales['nombre'] = user.first_name
        datos_iniciales['apellido'] = user.last_name
        datos_iniciales['correo'] = user.email
        perfil = Perfil.objects.get(user=user)
        datos_iniciales['cedula'] = perfil.cedula
        datos_iniciales['telefono'] = perfil.telefono
        datos_iniciales['consejo_comunal_temp'] = perfil.consejo_comunal
        return datos_iniciales

    def form_valid(self, form):

        if User.objects.filter(username=self.request.user.username):
            user = User.objects.get(username=self.request.user.username)
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
