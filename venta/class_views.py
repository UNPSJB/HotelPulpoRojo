from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView #View
from django.urls import reverse_lazy
from .forms import AlquilerForm
from .models import Alquiler, Factura, Liquidacion
from hotel.models import Habitacion, Hotel


    


class AlquilerCreate(CreateView):
    model = Alquiler
    form_class = AlquilerForm
    template_name = 'crear_alquiler.html'
    success_url = reverse_lazy('listar_habitaciones')