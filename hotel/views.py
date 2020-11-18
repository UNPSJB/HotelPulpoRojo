from django.shortcuts import render,redirect

# Create your views here.
from core.models import Vendedor
from .models import Hotel
from .forms import HotelForm, AsignarForm

def listarHotel(request):
    hoteles = Hotel.objects.all() #select * from Hotel
    contexto = { 
        'hoteles':hoteles
        }
    return render(request,'listar_hotel.html',contexto)

def info_hotel(request,id):
    hotel = Hotel.objects.get(id = id)
    asignar_form = AsignarForm(request.POST)
    contexto = { 
        'hotel':hotel,
        'lista_servicios': hotel.servicios.all(),
        'lista_vendedores': hotel.vendedores.all(),
        'asignar_form': asignar_form
    }
    return render(request,'info_hotel.html',contexto)
    
def desasignar_vendedor(request,id):
    pass

def asignar_vendedor(request,id):
    pass
