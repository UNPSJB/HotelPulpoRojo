from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request, HttpRequest
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView #View
from django.urls import reverse_lazy
from .forms import AlquilerForm
from .models import Alquiler, Factura, Liquidacion
from hotel.models import Hotel, Habitacion
# from core.models import Vendedor
from datetime import datetime




class AlquilerCreate(CreateView):
    model = Alquiler
    form_class = AlquilerForm
    template_name = 'crear_alquiler.html'
    success_url = reverse_lazy('alquilar_habitacion')



    def get_initial(self):
        hab = self.request.GET['habitacion']
        fecha_desde = self.request.GET['fecha_desde']
        fecha_hasta = self.request.GET['fecha_hasta']
        huespedes = int(self.request.GET['huespedes'])
        
        vendedor = self.request.user.id

        room = Habitacion.objects.get(id=hab)
        inicio = datetime.strptime(fecha_desde, '%d/%m/%Y').date()
        fin = datetime.strptime(fecha_hasta, '%d/%m/%Y').date()
        total = room.precio_alquiler(inicio, fin)
        
        return {'habitacion': hab,
                'inicio': fecha_desde,
                'fin': fecha_hasta,
                'cantidad_huespedes': huespedes,
                'total': total,
                'vendedor': vendedor}

class AlquilerList(ListView):
    model = Alquiler
    template_name = 'listar_alquiler.html'