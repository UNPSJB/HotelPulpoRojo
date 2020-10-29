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
from core.views import iniciarSesion, cerrarSesion, tipoHabitacion, index
from hotel.views import listarHotel
from core.class_views import PersonaCreate, PersonaDelete, PersonaList, PersonaUpdate
from core.class_views import TipoHabitacionCreate, TipoHabitacionList, TipoHabitacionUpdate, TipoHabitacionDelete
from hotel.class_views import HotelCreate,HotelDelete,HotelList,HotelUpdate

urlpatterns = [

    #Views
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    
    #Class_view
    #Core
    path('iniciar_sesion/', iniciarSesion, name = 'iniciar_sesion'),
    path('cerrar_sesion/', cerrarSesion, name = 'cerrar_sesion'),    
    
    #core
    path('', include('core.urls')),
    #hotel
    path('', include('hotel.urls')),
    #venta
    path('', include('venta.urls')),
    
]
