from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView #View
from django.urls import reverse_lazy
from .forms import PersonaForm, ClienteForm, CrearVendedorForm, EditarVendedorForm, EncargadoForm, LocalidadForm, ProvinciaForm, PaisForm
from .models import Persona, Provincia, Localidad, Pais

# Persona
class PersonaList(ListView):
    model = Persona
    template_name = 'listar_persona.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_persona')

#cliente
class ClienteList(ListView):
    model = Persona
    template_name = 'listar_cliente.html'

class ClienteCreate(CreateView):
    model = Persona
    form_class = ClienteForm
    template_name = 'crear_cliente.html'
    success_url = reverse_lazy('listar_cliente')

class ClienteUpdate(UpdateView):
    model = Persona
    form_class = ClienteForm
    template_name = 'crear_cliente.html'
    success_url = reverse_lazy('listar_cliente')

class ClienteDelete(DeleteView):
    model = Persona
    template_name = 'verificacion_cliente.html'
    success_url = reverse_lazy('listar_cliente')

#Encargado
class EncargadoCreate(CreateView):
    model = Persona
    form_class = EncargadoForm
    template_name = 'crear_encargado.html'
    success_url = reverse_lazy('listar_persona')

class EncargadoUpdate(UpdateView):
    model = Persona
    form_class = EncargadoForm
    template_name = 'crear_encargado.html'
    success_url = reverse_lazy('listar_persona')

class EncargadoDelete(DeleteView):
    model = Persona
    template_name = 'verificacion_encargado.html'
    success_url = reverse_lazy('listar_persona')

#Vendedor
class VendedorCreate(CreateView):
    model = Persona
    form_class = CrearVendedorForm
    template_name = 'crear_vendedor.html'
    success_url = reverse_lazy('listar_persona')

class VendedorUpdate(UpdateView):
    model = Persona
    form_class = EditarVendedorForm
    template_name = 'crear_vendedor.html'
    success_url = reverse_lazy('listar_persona')

class VendedorDelete(DeleteView):
    model = Persona
    template_name = 'verificacion_vendedor.html'
    success_url = reverse_lazy('listar_persona')


# Zona
class ZonaList(ListView):
    model = Localidad
    template_name = 'listar_zona.html'

class LocalidadCreate(CreateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'crear_localidad.html'
    success_url = reverse_lazy('listar_zona')
class ProvinciaCreate(CreateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'crear_provincia.html'
    success_url = reverse_lazy('listar_zona')
class PaisCreate(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'crear_pais.html'
    success_url = reverse_lazy('listar_zona')

class LocalidadUpdate(UpdateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'crear_localidad.html'
    success_url = reverse_lazy('listar_zona')
class ProvinciaUpdate(UpdateView):
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'crear_provincia.html'
    success_url = reverse_lazy('listar_zona')
class PaisUpdate(UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'crear_pais.html'
    success_url = reverse_lazy('listar_zona')

class LocalidadDelete(DeleteView):
    model = Localidad
    template_name = 'verificacion_zona.html'
    success_url = reverse_lazy('listar_zona')
class ProvinciaDelete(DeleteView):
    model = Provincia
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_zona')
class PaisDelete(DeleteView):
    model = Pais
    template_name = 'verificacion.html'
    success_url = reverse_lazy('listar_zona')