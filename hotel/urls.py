from django.urls import path
from hotel.class_views import HotelCreate, HotelDelete, HotelList, HotelUpdate
from hotel.class_views import HabitacionCreate, HabitacionDelete, HabitacionList, HabitacionUpdate
#from .views import (aca ponen las funciones de views que quieran importar)
#from .class_views import (aca ponen las funciones de class_views que quieran importar)

urlpatterns = [

    #Hotel
    path('listar_hotel/',HotelList.as_view() ,name = 'listar_hotel'),
    path('crear_hotel/',HotelCreate.as_view(),name = 'crear_hotel'),
    path('editar_hotel/<int:pk>/',HotelUpdate.as_view(),name = 'editar_hotel'),
    path('eliminar_hotel/<int:pk>/', HotelDelete.as_view(), name = 'eliminar_hotel'),
    
    #Habitacion
    path('listar_habitacion/',HabitacionList.as_view() ,name = 'listar_habitacion'),
    path('crear_habitacion/',HabitacionCreate.as_view(),name = 'crear_habitacion'),
    path('editar_habitacion/<int:pk>/',HabitacionUpdate.as_view(),name = 'editar_habitacion'),
    path('eliminar_habitacion/<int:pk>/', HabitacionDelete.as_view(), name = 'eliminar_habitacion'),
]
