from django.urls import path
from hotel.class_views import HotelCreate, HotelDelete, HotelList, HotelUpdate
from hotel.class_views import PaqueteTuristicoCreate, PaqueteTuristicoDelete, PaqueteTuristicoList, PaqueteTuristicoUpdate
from hotel.class_views import HabitacionCreate, HabitacionDelete, HabitacionList, HabitacionUpdate
from hotel.views import info_hotel, desasignar_vendedor, asignar_vendedor
from hotel.class_views import DescuentoCreate, DescuentoDelete, DescuentoUpdate, DescuentoList

urlpatterns = [

    #Hotel
    path('listar_hotel/',HotelList.as_view() ,name = 'listar_hotel'),
    path('afiliar_hotel/',HotelCreate.as_view(),name = 'afiliar_hotel'),
    path('editar_hotel/<int:pk>/',HotelUpdate.as_view(),name = 'editar_hotel'),
    path('eliminar_hotel/<int:pk>/', HotelDelete.as_view(), name = 'eliminar_hotel'),
    path('info_hotel/<int:id>/', info_hotel, name='info_hotel'),
    path('desasignar_vendedor/<int:id>/', desasignar_vendedor, name='desasignar_vendedor'),
    path('asignar_vendedor/<int:id>', asignar_vendedor, name='asignar_vendedor'),
    
    #Paquete Turistico
    path('info_hotel/<int:id>/listar_paquete_turistico/',PaqueteTuristicoList.as_view() ,name = 'listar_paquete_turistico'),
    path('crear_paquete_turistico/',PaqueteTuristicoCreate.as_view(),name = 'crear_paquete_turistico'),
    path('editar_paquete_turistico/<int:pk>/',PaqueteTuristicoUpdate.as_view(),name = 'editar_paquete_turistico'),
    path('eliminar_paquete_turistico/<int:pk>/',PaqueteTuristicoDelete.as_view(),name = 'eliminar_paquete_turistico'),
    
    #Habitacion
    path('listar_habitacion/',HabitacionList.as_view() ,name = 'listar_habitacion'),
    path('crear_habitacion/',HabitacionCreate.as_view(),name = 'crear_habitacion'),
    path('editar_habitacion/<int:pk>/',HabitacionUpdate.as_view(),name = 'editar_habitacion'),
    path('eliminar_habitacion/<int:pk>/', HabitacionDelete.as_view(), name = 'eliminar_habitacion'),

    #Descuento
    path('listar_descuento/',DescuentoList.as_view() ,name = 'listar_descuento'),
    path('crear_descuento/',DescuentoCreate.as_view(),name = 'crear_descuento'),
    path('editar_descuento/<int:pk>/',DescuentoUpdate.as_view(),name = 'editar_descuento'),
    path('eliminar_descuento/<int:pk>/',DescuentoDelete.as_view(),name = 'eliminar_descuento'),
    
]
