from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView, DetailView #View
from django.urls import reverse_lazy
from .models import Hotel
from .forms import HotelForm, PaqueteTuristicoForm, HabitacionForm, TemporadaAltaForm
from core.forms import EncargadoForm
from .models import Hotel, PaqueteTuristico, Habitacion, TemporadaAlta
from core.models import Encargado

#Hotel
class HotelList(ListView):
    model = Hotel
    template_name = 'listar_hotel.html'

class HotelCreate(CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'afiliar_hotel.html'
    success_url = reverse_lazy('listar_hotel')


class HotelUpdate(UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'afiliar_hotel.html' #Reutiliza la vista del crear para no usar dos templates diferentes
    success_url = reverse_lazy('listar_hotel')
    
class HotelDelete(DeleteView):
    model = Hotel
    template_name = 'verificacion_hotel.html'
    success_url = reverse_lazy('listar_hotel')

    

#PaqueteTuristico

class PaqueteTuristicoList(ListView):
    model = PaqueteTuristico
    template_name = 'listar_paquete_turistico.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = PaqueteTuristico.objects.filter(hotel_id=self.kwargs['id'])
        return super(PaqueteTuristicoList, self).get_context_data(**kwargs)

class PaqueteTuristicoCreate(CreateView):
    model = PaqueteTuristico
    form_class = PaqueteTuristicoForm
    template_name = 'crear_paquete_turistico.html'
    success_url = reverse_lazy('listar_paquete_turistico')

class PaqueteTuristicoUpdate(UpdateView):
    model = PaqueteTuristico
    form_class = PaqueteTuristicoForm
    template_name = 'crear_paquete_turistico.html'
    success_url = reverse_lazy('listar_paquete_turistico')

class PaqueteTuristicoDelete(DeleteView):
    model = PaqueteTuristico
    template_name = 'verificacion_paquete_turistico.html'
    success_url = reverse_lazy('listar_paquete_turistico')

#Habitacion
class HabitacionList(ListView):
    model = Habitacion
    template_name = 'listar_habitacion.html'

class HabitacionCreate(CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'crear_habitacion.html'
    success_url = reverse_lazy('listar_habitacion')

class HabitacionUpdate(UpdateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = 'crear_habitacion.html'
    success_url = reverse_lazy('listar_habitacion')

class HabitacionDelete(DeleteView):
    model = Habitacion
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_habitacion')

#Temporada Alta
class TemporadaAltaList(ListView):
    model = TemporadaAlta
    template_name = 'listar_temporada_alta.html'

class TemporadaAltaCreate(CreateView):
    model = TemporadaAlta
    form_class = TemporadaAltaForm
    template_name = 'crear_temporada_alta.html'
    success_url = reverse_lazy('listar_temporada_alta')

class TemporadaAltaUpdate(UpdateView):
    model = TemporadaAlta
    form_class = TemporadaAltaForm
    template_name = 'crear_temporada_alta.html'
    success_url = reverse_lazy('listar_temporada_alta')

class TemporadaAltaDelete(DeleteView):
    model = TemporadaAlta
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_temporada_alta')