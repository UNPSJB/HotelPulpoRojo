from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView #View
from django.urls import reverse_lazy
from .models import Hotel
from .forms import HotelForm, PaqueteTuristicoForm, HabitacionForm, DescuentoForm
from core.forms import EncargadoForm
from .models import Hotel,PaqueteTuristico, Habitacion, Descuento
from core.models import Encargado, Vendedor

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
        kwargs['object_list'] = PaqueteTuristico.objects.filter(hotel_id=self.kwargs['hotel_pk'])
        
        return super(PaqueteTuristicoList, self).get_context_data(**kwargs)

class PaqueteTuristicoCreate(CreateView):
    model = PaqueteTuristico
    form_class = PaqueteTuristicoForm
    template_name = 'crear_paquete_turistico.html'

    def get_context_data(self, **kwargs):
        print(self.kwargs['hotel_pk'])
        return super(PaqueteTuristicoCreate, self).get_context_data(**kwargs)

    def form_valid(self, form):
        hotel = Hotel.objects.get(id=self.kwargs.get('hotel_pk'))
        paquete = form.save(commit=False)
        paquete.hotel = hotel
        #article.save()  # This is redundant, see comments.
        return super(PaqueteTuristicoCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('info_hotel', kwargs={'id': self.kwargs.get('hotel_pk')})



class PaqueteTuristicoUpdate(UpdateView):
    model = PaqueteTuristico
    form_class = PaqueteTuristicoForm
    template_name = 'crear_paquete_turistico.html'

    def get_success_url(self):
        paqueteTuristico = PaqueteTuristico.objects.get(id=self.kwargs.get('pk'))
        return reverse_lazy('listar_paquete_turistico', kwargs={'hotel_pk': paqueteTuristico.hotel.pk})




class PaqueteTuristicoDelete(DeleteView):
    model = PaqueteTuristico
    template_name = 'verificacion_paquete_turistico.html'

    def get_success_url(self):
        paqueteTuristico = PaqueteTuristico.objects.get(id=self.kwargs.get('pk'))
        return reverse_lazy('listar_paquete_turistico', kwargs={'hotel_pk': paqueteTuristico.hotel.pk})
    
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

#Descuento
class DescuentoList(ListView):
    model = Descuento
    template_name = 'listar_descuento.html'

class DescuentoCreate(CreateView):
    model = Descuento
    form_class = DescuentoForm
    template_name = 'crear_descuento.html'
    success_url = reverse_lazy('listar_descuento')

class DescuentoUpdate(UpdateView):
    model = Descuento
    form_class = DescuentoForm
    template_name = 'crear_descuento.html' #Reutiliza la vista del crear para no usar dos templates diferentes
    success_url = reverse_lazy('listar_descuento')
    
class DescuentoDelete(DeleteView):
    model = Descuento
    template_name = 'verificacion_descuento.html'
    success_url = reverse_lazy('listar_descuento')
