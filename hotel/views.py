from django.shortcuts import render,redirect

# Create your views here.
from .models import Hotel
from .forms import HotelForm

def listarHotel(request):
    hoteles = Hotel.objects.all() #select * from Hotel
    contexto = { 
        'hoteles':hoteles
        }
    return render(request,'listar_hotel.html',contexto)

# def crearHotel(request):
#     if request.method == 'GET':
#         form = HotelForm()
#         contexto = {
#             'form':form
#             }
#     else:
#         form = HotelForm(request.POST)
#         contexto = {
#             'form':form
#         }
#         if form.is_valid():
#             form.save()
#             return redirect('listar_persona')
#     return render(request,'crear_persona.html',contexto)

# def editarPersona(request,id):
#     persona = Hotel.objects.get(id = id)
#     if request.method == 'GET':
#         form = HotelForm(instance=persona)
#         contexto = {
#             'form':form
#         }
#     else:
#         form = PersonaForm(request.POST,instance=persona)
#         contexto = {
#             'form':form
#         }
#         if form.is_valid():
#             form.save()
#             return redirect('listar_persona')
#     return render(request,'crear_persona.html',contexto)

# def eliminarPersona(request,id):
#     persona = Persona.objects.get(id = id)
#     persona.delete()
#     return redirect('listar_persona')

def info_hotel(request,id):
    hotel = Hotel.objects.get(id = id)
    contexto = { 
        'hotel':hotel
    }
    return render(request,"info_hotel.html",contexto)
