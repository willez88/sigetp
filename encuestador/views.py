from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from .models import Encuestador
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import EncuestadorForm

# Create your views here.

class EncuestadorList(ListView):
    model = Encuestador
    template_name = "encuestador.lista.html"

class EncuestadorCreate(CreateView):
    model = Encuestador
    form_class = EncuestadorForm
    template_name = "encuestador.registro.html"
    success_url = reverse_lazy('encuestador_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.nombre = form.cleaned_data['nombre']
        self.object.apellido = form.cleaned_data['apellido']
        self.object.cedula = form.cleaned_data['cedula']
        self.object.telefono = form.cleaned_data['telefono']
        self.object.correo = form.cleaned_data['correo']
        self.object.save()
        return super(EncuestadorCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(EncuestadorCreate, self).form_invalid(form)

class EncuestadorUpdate(UpdateView):
    model = Encuestador
    form_class = EncuestadorForm
    template_name = "encuestador.registro.html"
    success_url = reverse_lazy('encuestador_lista')

class EncuestadorDelete(DeleteView):
    model = Encuestador
    template_name = "encuestador.eliminar.html"
    success_url = reverse_lazy('encuestador_lista')

