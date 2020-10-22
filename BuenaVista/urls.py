"""BuenaVista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import iniciarSesion, cerrarSesion, index
from hotel.views import listarHotel
from core.class_views import PersonaCreate,PersonaDelete,PersonaList,PersonaUpdate
from hotel.class_views import HotelCreate,HotelDelete,HotelList,HotelUpdate

urlpatterns = [

    #Views
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    
    #path('listar_persona/',listarPersona,name = 'listar_persona'),
    #path('crear_persona/',crearPersona,name = 'crear_persona'),
    #path('editar_persona/<int:id>/',editarPersona,name = 'editar_persona'),
    #path('eliminar_persona/<int:id>/', eliminarPersona, name = 'eliminar_persona'),

    #Class_view
    #Core
    path('iniciar_sesion/', iniciarSesion, name = 'iniciar_sesion'),
    path('cerrar_sesion/', cerrarSesion, name = 'cerrar_sesion'),
    #Persona
    path('listar_persona/',PersonaList.as_view() ,name = 'listar_persona'),
    path('crear_persona/',PersonaCreate.as_view(),name = 'crear_persona'),
    path('editar_persona/<int:pk>/',PersonaUpdate.as_view(),name = 'editar_persona'),
    path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(), name = 'eliminar_persona'),
    #Hotel
    path('listar_hotel/',HotelList.as_view() ,name = 'listar_hotel'),
    path('crear_hotel/',HotelCreate.as_view(),name = 'crear_hotel'),
    path('editar_hotel/<int:pk>/',HotelUpdate.as_view(),name = 'editar_hotel'),
    path('eliminar_hotel/<int:pk>/', HotelDelete.as_view(), name = 'eliminar_hotel'),
    #Zona
    path('', include('core.urls')),
    
    
    
    #Categoria

    #Servicio

    #Tipo de Habitación


]
