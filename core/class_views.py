from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView #View
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona
from .forms import TipoHabitacionForm
from .models import TipoHabitacion

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
    success_url = reverse_lazy('index')
