from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request, HttpRequest
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
    request = HttpRequest()
    request.method = 'GET'
    hues = request.GET.get('cantidad_huespedes','no funco')
    print(hues)


    # def get_initial(self):
    #     return {'cantidad_huespedes':4}

    # def get_params(self, request):
    #     return request.GET.get('habitacion')

    # def get_initial(self):
    #     habitacion = self.get_params()
    #     print(habitacion)
    #     # fecha_desde = request.GET.get('fecha_desde')
    #     # fecha_hasta = request.GET.get('fecha_hasta')
    #     # huespedes = request.GET.get('huespedes')
    #     return {'habitacion': habitacion}
        # return {'habitacion': habitacion, 'fecha_desde': fecha_desde, 'fecha_hasta': fecha_hasta, 'huespedes': huespedes}