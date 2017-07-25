from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import GrupoFamiliar
from .forms import GrupoFamiliarForm
from vivienda.models import Vivienda

# Create your views here.

class GrupoFamiliarList(ListView):
    model = GrupoFamiliar
    template_name = "grupo.familiar.lista.html"

    def get_queryset(self):
        queryset = GrupoFamiliar.objects.filter(vivienda__user=self.request.user)
        return queryset

class GrupoFamiliarCreate(CreateView):
    model = GrupoFamiliar
    form_class = GrupoFamiliarForm
    template_name = "grupo.familiar.registro.html"
    success_url = reverse_lazy('grupo_familiar_lista')

    def form_valid(self, form):

        vivienda = Vivienda.objects.get(pk=form.cleaned_data['vivienda'])
        self.object = form.save(commit=False)
        self.object.vivienda = vivienda
        self.object.apellido_familia = form.cleaned_data['apellido_familia']
        if form.cleaned_data['familia_beneficiada']:
            self.object.familia_beneficiada = form.cleaned_data['familia_beneficiada']
        self.object.tenencia = form.cleaned_data['tenencia']
        if form.cleaned_data['tenencia'] == 'AL':
            self.object.alquilada = form.cleaned_data['alquilada']
        if form.cleaned_data['pasaje']:
            self.object.pasaje = form.cleaned_data['pasaje']
        self.object.save()
        return super(GrupoFamiliarCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(GrupoFamiliarCreate, self).form_invalid(form)

class GrupoFamiliarUpdate(UpdateView):
    model = GrupoFamiliar
    form_class = GrupoFamiliarForm
    template_name = "grupo.familiar.registro.html"
    success_url = reverse_lazy('grupo_familiar_lista')

class GrupoFamiliarDelete(DeleteView):
    model = GrupoFamiliar
    template_name = "grupo.familiar.eliminar.html"
    success_url = reverse_lazy('grupo_familiar_lista')

