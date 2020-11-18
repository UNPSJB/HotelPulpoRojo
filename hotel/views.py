from django.shortcuts import render,redirect, get_object_or_404

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
    
def desasignar_vendedor(request,hotel_pk, vendedor_pk):
    hotel = get_object_or_404(Hotel, id = hotel_pk)
    # hotel = Hotel.objects.get(id = hotel_pk)
    vendedor = get_object_or_404(Vendedor, id = vendedor_pk)
    # vendedor = Vendedor.objects.get(id = vendedor_pk)
    hotel.vendedores.remove(vendedor)
    return redirect('info_hotel', hotel_pk)

def asignar_vendedor(request, hotel_pk):
    hotel = Hotel.objects.get(id = hotel_pk)
    asignarform = AsignarForm(request.POST)
    asignarform.save(hotel)
    print(hotel_pk)
    print(request.POST)
    
    return redirect('info_hotel', hotel_pk)
