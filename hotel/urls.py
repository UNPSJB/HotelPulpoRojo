from django.urls import path
from hotel.class_views import HotelCreate, HotelDelete, HotelList, HotelUpdate
#from .views import (aca ponen las funciones de views que quieran importar)
#from .class_views import (aca ponen las funciones de class_views que quieran importar)

urlpatterns = [

    #Hotel
    path('listar_hotel/',HotelList.as_view() ,name = 'listar_hotel'),
    path('afiliar_hotel/',HotelCreate.as_view(),name = 'afiliar_hotel'),
    path('editar_hotel/<int:pk>/',HotelUpdate.as_view(),name = 'editar_hotel'),
    path('eliminar_hotel/<int:pk>/', HotelDelete.as_view(), name = 'eliminar_hotel'),
    
]
