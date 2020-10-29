from django.urls import path
#from .views import (aca ponen las funciones de views que quieran importar)
from .class_views import PersonaCreate, PersonaDelete, PersonaUpdate, PersonaList
from .class_views import ClienteCreate, ClienteDelete, ClienteUpdate, ClienteList
from .class_views import VendedorCreate, VendedorDelete, VendedorUpdate
from .class_views import EncargadoCreate, EncargadoDelete, EncargadoUpdate
from .class_views import ZonaList, PaisCreate, ProvinciaCreate, LocalidadCreate, PaisUpdate, LocalidadUpdate, ProvinciaUpdate, LocalidadDelete, ProvinciaDelete, PaisDelete

urlpatterns = [
    #Persona
    path('listar_persona/',PersonaList.as_view() ,name = 'listar_persona'),
    path('crear_persona/',PersonaCreate.as_view(),name = 'crear_persona'),
    path('editar_persona/<int:pk>/',PersonaUpdate.as_view(),name = 'editar_persona'),
    path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(), name = 'eliminar_persona'),

    #Cliente
    path('listar_cliente',ClienteList.as_view(), name = 'listar_cliente'),
    path('crear_cliente/',ClienteCreate.as_view(),name = 'crear_cliente'),
    path('editar_cliente/<int:pk>/',ClienteUpdate.as_view(),name = 'editar_cliente'),
    path('eliminar_cliente/<int:pk>/', ClienteDelete.as_view(), name = 'eliminar_cliente'),

    #Encargado
    path('crear_encargado/',EncargadoCreate.as_view(),name = 'crear_encargado'),
    path('editar_encargado/<int:pk>/',EncargadoUpdate.as_view(),name = 'editar_encargado'),
    path('eliminar_encargado/<int:pk>/', EncargadoDelete.as_view(), name = 'eliminar_encargado'),

    #Vendedor
    path('crear_vendedor/',VendedorCreate.as_view(),name = 'crear_vendedor'),
    path('editar_vendedor/<int:pk>/',VendedorUpdate.as_view(),name = 'editar_vendedor'),
    path('eliminar_vendedor/<int:pk>/', VendedorDelete.as_view(), name = 'eliminar_vendedor'),


    #Zona
    path('listar_zona/', ZonaList.as_view(),name = 'listar_zona'),

    path('crear_pais/', PaisCreate.as_view(),name = 'crear_pais'),
    path('crear_localidad/', LocalidadCreate.as_view(),name = 'crear_localidad'),
    path('crear_provincia/', ProvinciaCreate.as_view(),name = 'crear_provincia'),

    path('editar_localidad/<int:pk>/', LocalidadUpdate.as_view(),name = 'editar_localidad'),
    path('editar_provincia/<int:pk>/', ProvinciaUpdate.as_view(),name = 'editar_provincia'),
    path('editar_pais/<int:pk>/', PaisUpdate.as_view(),name = 'editar_pais'),

    path('eliminar_localidad/<int:pk>/', LocalidadDelete.as_view(), name = 'eliminar_localidad'),
    path('eliminar_provincia/<int:pk>/', ProvinciaDelete.as_view(), name = 'eliminar_provincia'),
    path('eliminar_pais/<int:pk>/', PaisDelete.as_view(), name = 'eliminar_pais'),
]
