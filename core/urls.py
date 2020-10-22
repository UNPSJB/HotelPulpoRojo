from django.urls import path
from . import views
#from . import class_views
#from .views import 
from .class_views import ZonaList, PaisCreate, ProvinciaCreate, LocalidadCreate, PaisUpdate, LocalidadUpdate, ProvinciaUpdate, LocalidadDelete, ProvinciaDelete, PaisDelete

urlpatterns = [
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
