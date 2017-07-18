from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import Persona
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PersonaForm
from vivienda.grupo_familiar.models import GrupoFamiliar
import datetime

# Create your views here.

class PersonaList(ListView):
    model = Persona
    template_name = "persona.lista.html"

    def get_queryset(self):
        queryset = Persona.objects.filter(grupo_familiar__vivienda__user=self.request.user)
        return queryset

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona.registro.html"
    success_url = reverse_lazy('persona_lista')

    def form_valid(self, form):
        grupo_familiar = GrupoFamiliar.objects.get(pk=form.cleaned_data['grupo_familiar'])
        self.object = form.save(commit=False)
        self.object.grupo_familiar = grupo_familiar
        self.object.nombre = form.cleaned_data['nombre']
        self.object.apellido = form.cleaned_data['apellido']
        if form.cleaned_data['tiene_cedula']:
            self.object.cedula = form.cleaned_data['cedula']
        self.object.telefono = form.cleaned_data['telefono']
        self.object.correo = form.cleaned_data['correo']
        self.object.sexo = form.cleaned_data['sexo']
        self.object.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        self.object.parentesco = form.cleaned_data['parentesco']
        self.object.estado_civil = form.cleaned_data['estado_civil']
        self.object.grado_instruccion = form.cleaned_data['grado_instruccion']
        self.object.mision_educativa = form.cleaned_data['mision_educativa']
        self.object.profesion = form.cleaned_data['profesion']
        self.object.ocupacion = form.cleaned_data['ocupacion']
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
        self.object.save()
        return super(PersonaCreate, self).form_valid(form)

        def form_invalid(self, form):
            return super(PersonaCreate, self).form_invalid(form)

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = "persona.registro.html"
    success_url = reverse_lazy('persona_lista')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = "persona.eliminar.html"
    success_url = reverse_lazy('persona_lista')
