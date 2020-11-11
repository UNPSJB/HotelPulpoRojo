from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView #View
from django.urls import reverse_lazy
from .forms import HotelForm
from core.forms import EncargadoForm
from .models import Hotel
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