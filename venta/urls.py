from django.urls import path, re_path
from django.conf.urls import url
from .views import alquilar_habitacion
from .class_views import AlquilerCreate, AlquilerList



urlpatterns = [
    path('alquilar_habitacion/', alquilar_habitacion, name='alquilar_habitacion'),
    path('crear_alquiler/', AlquilerCreate.as_view(),name = 'crear_alquiler'),
    path('listar_alquiler/', AlquilerList.as_view(), name = 'listar_alquiler'),
]