from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView #View
from django.urls import reverse_lazy
from .forms import HotelForm, HabitacionForm
from .models import Hotel, Habitacion

#Hotel
class HotelList(ListView):
    model = Hotel
    template_name = 'listar_hotel.html'

class HotelCreate(CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'crear_hotel.html'
    success_url = reverse_lazy('listar_hotel')

class HotelUpdate(UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'crear_hotel.html'
    success_url = reverse_lazy('listar_hotel')

class HotelDelete(DeleteView):
    model = Hotel
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_hotel')

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