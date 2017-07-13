from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vivienda, Imagen
from .forms import ViviendaForm, ViviendaUpdateForm, ImagenForm
from django.contrib.auth.models import User
from base.models import ConsejoComunal

# Create your views here.

class ViviendaList(ListView):
    model = Vivienda
    template_name = "vivienda.lista.html"

    def get_queryset(self):
        queryset = Vivienda.objects.filter(user=self.request.user)
        return queryset

class ViviendaCreate(CreateView):
    model = Vivienda
    form_class = ViviendaForm
    template_name = "vivienda.registro.html"
    success_url = reverse_lazy('vivienda_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)

        user = User.objects.get(user__username=self.request.user.username)
        self.object.user = user

        self.object.fecha_hora = form.cleaned_data['fecha_hora']
        self.object.tipo_techo = form.cleaned_data['tipo_techo']
        self.object.servicio_electrico = form.cleaned_data['servicio_electrico']
        self.object.situacion_sanitaria = form.cleaned_data['situacion_sanitaria']
        self.object.disposicion_basura = form.cleaned_data['disposicion_basura']
        self.object.disposicion_basura = form.cleaned_data['disposicion_basura']
        self.object.tipo_vivienda = form.cleaned_data['tipo_vivienda']
        self.object.tipo_pared = form.cleaned_data['tipo_pared']

        if form.cleaned_data['tipo_pared'] == 'BL':
            self.object.pared_frizada = form.cleaned_data['pared_frizada']

        self.object.tipo_piso = form.cleaned_data['tipo_piso']

        if form.cleaned_data['tipo_piso'] == 'CE':
            self.object.tipo_cemento = form.cleaned_data['tipo_cemento']

        self.object.condicion_vivienda = form.cleaned_data['condicion_vivienda']
        self.object.condicion_techo = form.cleaned_data['condicion_techo']
        self.object.condicion_pared = form.cleaned_data['condicion_pared']
        self.object.condicion_piso = form.cleaned_data['condicion_piso']
        self.object.condicion_ventilacion = form.cleaned_data['condicion_ventilacion']
        self.object.condicion_iluminacion = form.cleaned_data['condicion_iluminacion']
        self.object.accesibilidad_ambulatorio = form.cleaned_data['accesibilidad_ambulatorio']
        self.object.accesibilidad_escuela = form.cleaned_data['accesibilidad_escuela']
        self.object.accesibilidad_liceo = form.cleaned_data['accesibilidad_liceo']
        self.object.accesibilidad_centro_abastecimiento = form.cleaned_data['accesibilidad_centro_abastecimiento']
        self.object.numero_habitaciones = form.cleaned_data['numero_habitaciones']
        self.object.numero_salas = form.cleaned_data['numero_salas']
        self.object.numero_banhos = form.cleaned_data['numero_banhos']

        if form.cleaned_data['tiene_terreno']:
            self.object.tiene_terreno = form.cleaned_data['tiene_terreno']
            self.object.metro_cuadrado = form.cleaned_data['metro_cuadrado']
            self.object.productivo = form.cleaned_data['productivo']
            self.object.por_producir = form.cleaned_data['por_producir']
        else:
            self.object.metro_cuadrado = 0.0
            self.object.productivo = 0.0
            self.object.por_producir = 0.0

        if form.cleaned_data['riesgo_rio']:
            self.object.riesgo_rio = form.cleaned_data['riesgo_rio']

        if form.cleaned_data['riesgo_quebrada']:
            self.object.riesgo_quebrada = form.cleaned_data['riesgo_quebrada']

        if form.cleaned_data['riesgo_derrumbe']:
            self.object.riesgo_derrumbe = form.cleaned_data['riesgo_derrumbe']

        if form.cleaned_data['riesgo_zona_sismica']:
            self.object.riesgo_zona_sismisca = form.cleaned_data['riesgo_zona_sismica']

        self.object.animales = form.cleaned_data['animales']

        self.object.consejo_comunal = form.cleaned_data['consejo_comunal']

        self.object.direccion = form.cleaned_data['direccion']
        self.object.numero_vivienda = form.cleaned_data['numero_vivienda']
        self.object.coordenadas = form.cleaned_data['coordenada']

        self.object.save()
        return super(ViviendaCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(ViviendaCreate, self).form_invalid(form)

class ViviendaUpdate(UpdateView):
    model = Vivienda
    form_class = ViviendaUpdateForm
    template_name = "vivienda.registro.html"
    success_url = reverse_lazy('vivienda_lista')

    def get_initial(self):
        datos_iniciales = super(ViviendaUpdate, self).get_initial()
        vivienda = Vivienda.objects.get(pk=self.request.user.id)
        datos_iniciales['coordenada'] = vivienda.coordenadas.split(",")
        return datos_iniciales

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.coordenadas = form.cleaned_data['coordenada']
        self.object.save()
        return super(ViviendaUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(ViviendaUpdate, self).form_invalid(form)

class ViviendaDelete(DeleteView):
    model = Vivienda
    template_name = "vivienda.eliminar.html"
    success_url = reverse_lazy('vivienda_lista')

class ImagenList(ListView):
    model = Imagen
    template_name = "imagen.lista.html"

    def get_queryset(self):
        queryset = Imagen.objects.filter(vivienda__user=self.request.user)
        return queryset

class ImagenCreate(CreateView):
    model = Imagen
    form_class = ImagenForm
    template_name = "imagen.registro.html"
    success_url = reverse_lazy('vivienda_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        vivienda = Vivienda.objects.filter(pk=form.cleaned_data['vivienda']).get()
        self.object.vivienda = vivienda
        self.object.imagen = form.cleaned_data['imagen']
        self.object.save()
        return super(ImagenCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ImagenCreate, self).form_invalid(form)

