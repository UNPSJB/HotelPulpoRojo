from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, request, HttpRequest
from .models import Factura
from core.models import Vendedor, Localidad
from hotel.models import *



def alquilar_habitacion(request):
    habitaciones = Habitacion.objects.all()
    destino = ""
    inicio_texto = ""
    fin_texto = ""
    huespedes = ""
    

    #Esta es la parte de la búsqueda/filtro
    if request.method == 'POST':
        # Si el usuario no ingresa una cantidad de huespedes, tomamos como predeterminado que busca por al menos 1 huesped
        if (request.POST.get('huespedes') == ''):
            huespedes=1
        else:
            huespedes = int(request.POST.get('huespedes'))
        destino = request.POST.get('destino')
        fecha_desde = request.POST.get('fecha_desde')
        fecha_hasta = request.POST.get('fecha_hasta')
        inicio_texto = fecha_desde
        fin_texto = fecha_hasta
        fecha_desde = datetime.strptime(fecha_desde, '%d/%m/%Y').date()
        fecha_hasta = datetime.strptime(fecha_hasta, '%d/%m/%Y').date()
        habitaciones = Habitacion.objects.exclude(alquileres__inicio__lte=fecha_desde, alquileres__fin__gte=fecha_hasta)

        # Esta es la búsqueda que hace cuando tiene ingresada una cantidad de huespedes, y un destino
        if (destino != '' and huespedes != ''):
            zona = Localidad.objects.crear_zona(destino)
            habitaciones = Habitacion.objects.filter(hotel__localidad__in=zona, tipo__pasajeros__gte=huespedes).exclude(alquileres__inicio__lte=fecha_desde, alquileres__fin__gte=fecha_hasta)
            return render(request, "alquilar_habitacion.html", {'habitaciones': habitaciones,
                                                                "destino": destino,
                                                                "fecha_desde": inicio_texto,
                                                                "fecha_hasta": fin_texto,
                                                                "huespedes": huespedes})
        # Esta es la búsqueda que hace cuando el usuario ingresa la cantidad de huespedes
        elif (destino == ''):
            habitaciones = Habitacion.objects.filter(tipo__pasajeros__gte=huespedes).exclude(alquileres__inicio__lte=fecha_desde, alquileres__fin__gte=fecha_hasta)
            return render(request, "alquilar_habitacion.html", {'habitaciones': habitaciones,
                                                                "fecha_desde": inicio_texto,
                                                                "fecha_hasta": fin_texto,
                                                                "huespedes": huespedes})

    # Esta es la búsqueda predeterminada, donde solo tenemos el rango de fechas
    return render(request, "alquilar_habitacion.html", {'habitaciones': habitaciones,
                                                        "fecha_desde": inicio_texto,
                                                        "fecha_hasta": fin_texto})
