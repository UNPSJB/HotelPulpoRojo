from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView #View
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona
from .forms import TipoHabitacionForm, PersonaForm, LocalidadForm, ProvinciaForm, PaisForm
from .models import TipoHabitacion, Persona, Provincia,Localidad,Pais

# Persona
class PersonaList(ListView):
    model = Persona
    template_name = 'listar_persona.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_persona')

# Tipo habitacion
class TipoHabitacionCreate(CreateView):
    model = TipoHabitacion
    form_class = TipoHabitacionForm
    template_name = 'crear_tipo_habitacion.html'
    success_url = reverse_lazy('listar_tipo_habitacion')

class TipoHabitacionList(ListView):
    model = TipoHabitacion
    template_name = 'listar_tipo_habitacion.html'

class TipoHabitacionUpdate(UpdateView):
    model = TipoHabitacion
    form_class = TipoHabitacionForm
    template_name = 'crear_tipo_habitacion.html'
    success_url = reverse_lazy('listar_tipo_habitacion')

class TipoHabitacionDelete(DeleteView):
    model = TipoHabitacion
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_tipo_habitacion')
# Zona
class ZonaList(ListView):
    model = Localidad
    template_name = 'listar_zona.html'

class LocalidadCreate(CreateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'crear_localidad.html'
    success_url = reverse_lazy('listar_zona')
class ProvinciaCreate(CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'crear_provincia.html'
    success_url = reverse_lazy('crear_localidad')
class PaisCreate(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'crear_pais.html'
    success_url = reverse_lazy('crear_provincia')

class LocalidadUpdate(UpdateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'crear_localidad.html'
    success_url = reverse_lazy('listar_zona')
class ProvinciaUpdate(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'crear_provincia.html'
    success_url = reverse_lazy('listar_zona')
class PaisUpdate(UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'crear_pais.html'
    success_url = reverse_lazy('listar_zona')

class LocalidadDelete(DeleteView):
    model = Localidad
    template_name = 'verificacion_zona.html'
    success_url = reverse_lazy('listar_zona')
class ProvinciaDelete(DeleteView):
    model = Provincia
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_zona')
class PaisDelete(DeleteView):
    model = Pais
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_zona')
