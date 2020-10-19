from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView #View
from django.urls import reverse_lazy
from .forms import HotelForm
from .models import Hotel

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