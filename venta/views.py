from django.shortcuts import render

from .models import Factura
from core.models import Vendedor
from hotel.models import Habitacion, Hotel


def alquilar_habitacion(request):
    habitaciones = Habitacion.objects.all()
    
    # Parámetros de búsqueda:
    # localidad = NULL  # Filtro por defecto
    # fecha_desde
    # fecha_hasta
    # huespedes

    #Esta es la parte de la búsqueda/filtro
    # if request.POST.get('localidad', '', '', ''):
    #     localidad = request.POST.get('localidad')
    #     fecha_desde
    #     fecha_hasta
    #     huespedes = int(request.POST.get('huespedes'))
    #     habitaciones = habitaciones.filter(localidad=localidad)

    return render(request, "alquilar_habitacion.html", {'habtaciones': habitaciones})