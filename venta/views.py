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
        destino = request.POST.get('destino')
        huespedes = int(request.POST.get('huespedes'))
        fecha_desde = request.POST.get('fecha_desde')
        fecha_hasta = request.POST.get('fecha_hasta')
        inicio_texto = fecha_desde
        fin_texto = fecha_hasta
        fecha_desde = datetime.strptime(fecha_desde, '%d/%m/%Y').date()
        fecha_hasta = datetime.strptime(fecha_hasta, '%d/%m/%Y').date()

    if (destino != '' and huespedes != ''):
        zona = Localidad.objects.crear_zona(destino)
        habitaciones = Habitacion.objects.filter(hotel__localidad__in=zona, tipo__pasajeros__gte=huespedes).exclude(alquileres__inicio__lte=fecha_desde, alquileres__fin__gte=fecha_hasta)
        return render(request, "alquilar_habitacion.html", {'habitaciones': habitaciones,
                                                            "destino": destino,
                                                            "fecha_desde": inicio_texto,
                                                            "fecha_hasta": fin_texto,
                                                            "huespedes": huespedes})
    elif (destino == ''):
        habitaciones = Habitacion.objects.filter(tipo__pasajeros__gte=huespedes).exclude(alquileres__inicio__lte=fecha_desde, alquileres__fin__gte=fecha_hasta)
        return render(request, "alquilar_habitacion.html", {'habitaciones': habitaciones,
                                                            "fecha_desde": inicio_texto,
                                                            "fecha_hasta": fin_texto,
                                                            "huespedes": huespedes})
    elif (huespedes == ''):
        zona = Localidad.objects.crear_zona(destino)
        habitaciones = Habitacion.objects.filter(hotel__localidad__in=zona).exclude(alquileres__inicio__lte=fecha_desde, alquileres__fin__gte=fecha_hasta)
        return render(request, "alquilar_habitacion.html", {'habitaciones': habitaciones,
                                                            "destino": destino,
                                                            "fecha_desde": inicio_texto,
                                                            "fecha_hasta": fin_texto})

    habitaciones = Habitacion.objects.exclude(alquileres__inicio__lte=fecha_desde, alquileres__fin__gte=fecha_hasta)
    return render(request, "alquilar_habitacion.html", {'habitaciones': habitaciones,
                                                        "fecha_desde": inicio_texto,
                                                        "fecha_hasta": fin_texto})
