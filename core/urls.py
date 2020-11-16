from django.urls import path
#from .views import (aca ponen las funciones de views que quieran importar)
from .class_views import PersonaCreate, PersonaDelete, PersonaUpdate, PersonaList #Vistas de Persona
from .class_views import ClienteCreate, ClienteDelete, ClienteUpdate, ClienteList #Vistas de Cliente
from .class_views import VendedorCreate, VendedorDelete, VendedorUpdate #Vistas de Vendedor
from .class_views import EncargadoCreate, EncargadoDelete, EncargadoUpdate #Vistas de Encargado
from .class_views import AdministradorCreate, AdministradorDelete, AdministradorUpdate #Vistas de Administrador
from .class_views import ZonaList, PaisCreate, ProvinciaCreate, LocalidadCreate, PaisUpdate, LocalidadUpdate, ProvinciaUpdate, LocalidadDelete, ProvinciaDelete, PaisDelete #Vistas de Zonas
from .class_views import TipoHabitacionList, TipoHabitacionCreate, TipoHabitacionUpdate, TipoHabitacionDelete #Vistas de Tipo de Habitaci�n
from .class_views import ServicioList, ServicioCreate, ServicioUpdate#, ServicioDelete #Vistas de Servicio
from .class_views import CategoriaList, CategoriaCreate, CategoriaUpdate#, CategoriaDelete #Vistas de Categoria

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

    #Administrador
    path('crear_administrador/',AdministradorCreate.as_view(),name = 'crear_administrador'),
    path('editar_administrador/<int:pk>/',AdministradorUpdate.as_view(),name = 'editar_administrador'),
    path('eliminar_administrador/<int:pk>/', AdministradorDelete.as_view(), name = 'eliminar_administrador'),

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

    #Tipo habitacion
    path('listar_tipo_habitacion/', TipoHabitacionList.as_view(), name = 'listar_tipo_habitacion'),
    path('crear_tipo_habitacion/', TipoHabitacionCreate.as_view(), name = 'crear_tipo_habitacion'),
    path('editar_tipo_habitacion/<int:pk>/',TipoHabitacionUpdate.as_view(),name = 'editar_tipo_habitacion'),
    path('eliminar_tipo_habitacion/<int:pk>/', TipoHabitacionDelete.as_view(), name = 'eliminar_tipo_habitacion'),

    #Servicio
    path('listar_servicio/', ServicioList.as_view(), name = 'listar_servicio'),
    path('crear_servicio/', ServicioCreate.as_view(), name = 'crear_servicio'),
    path('editar_servicio/<int:pk>/', ServicioUpdate.as_view(), name = 'editar_servicio'),
    #path('eliminar_servicio/<int:pk>/', ServicioDelete.as_view(), name = 'eliminar_servicio')

    #Categoria
    path('listar_categoria/', CategoriaList.as_view(), name = 'listar_categoria'),
    path('crear_categoria/', CategoriaCreate.as_view(), name = 'crear_categoria'),
    path('editar_categoria/<int:pk>/', CategoriaUpdate.as_view(), name = 'editar_categoria'),
    #path('eliminar_categoria/<int:pk>/', CategoriaDelete.as_view(), name = 'eliminar_categoria')

]
