from django.urls import path
<<<<<<< HEAD
from hotel.class_views import HotelCreate, HotelDelete, HotelList, HotelUpdate, PaqueteTuristicoCreate, PaqueteTuristicoDelete, PaqueteTuristicoList, PaqueteTuristicoUpdate
from hotel.views import info_hotel
=======
from hotel.class_views import HotelCreate, HotelDelete, HotelList, HotelUpdate
from hotel.class_views import HabitacionCreate, HabitacionDelete, HabitacionList, HabitacionUpdate
#from .views import (aca ponen las funciones de views que quieran importar)
>>>>>>> 9079b605bd74e7daf48eb12161e9335c2720db17
#from .class_views import (aca ponen las funciones de class_views que quieran importar)

urlpatterns = [

    #Hotel
    path('listar_hotel/',HotelList.as_view() ,name = 'listar_hotel'),
    path('crear_hotel/',HotelCreate.as_view(),name = 'crear_hotel'),
    path('editar_hotel/<int:pk>/',HotelUpdate.as_view(),name = 'editar_hotel'),
    path('eliminar_hotel/<int:pk>/', HotelDelete.as_view(), name = 'eliminar_hotel'),
<<<<<<< HEAD
    path('info_hotel/<int:id>/', info_hotel, name='info_hotel'),
    #Paquete Turistico
    path('info_hotel/<int:id>/listar_paquete_turistico/',PaqueteTuristicoList.as_view() ,name = 'listar_paquete_turistico'),
    path('crear_paquete_turistico/',PaqueteTuristicoCreate.as_view(),name = 'crear_paquete_turistico'),
    path('editar_paquete_turistico/<int:pk>/',PaqueteTuristicoUpdate.as_view(),name = 'editar_paquete_turistico'),
    path('eliminar_paquete_turistico/<int:pk>/',PaqueteTuristicoDelete.as_view(),name = 'eliminar_paquete_turistico'),
=======
    
    #Habitacion
    path('listar_habitacion/',HabitacionList.as_view() ,name = 'listar_habitacion'),
    path('crear_habitacion/',HabitacionCreate.as_view(),name = 'crear_habitacion'),
    path('editar_habitacion/<int:pk>/',HabitacionUpdate.as_view(),name = 'editar_habitacion'),
    path('eliminar_habitacion/<int:pk>/', HabitacionDelete.as_view(), name = 'eliminar_habitacion'),
>>>>>>> 9079b605bd74e7daf48eb12161e9335c2720db17
]
