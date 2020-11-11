from django.shortcuts import render,redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .models import TipoHabitacion, Servicio, Categoria
from .forms import TipoHabitacionForm, ServicioForm, CategoriaForm
from django.views.generic import ListView, CreateView


def index(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "index.html")
    # En otro caso redireccionamos al login
    return redirect('/iniciar_sesion')


def iniciarSesion(request):
     # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "iniciar_sesion.html", {'form': form})

    #return render(request,'iniciar_sesion.html')

def cerrarSesion(request):
    #Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

#Tipo Habitacion
def tipoHabitacion(request):
    form = TipoHabitacionForm(request.POST)
    contexto = {
        'form':form
    }
    if form.is_valid():
        form.save()
        return redirect('listar_tipo_habitacion')
    return render(request,'crear_tipo_habitacion.html',contexto)

#Servicio
'''
def listarServicio(request):
    servicio = Servicio.objects.all()
    contexto = {'servicio':servicio}
    return render(request, '/listar_servicio.html', contexto)
'''
class ServicioList (ListView):
    model = Servicio
    template_name = 'templates/core/listar_servicio.html'

class ServicioCreate (CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'templates/core/crear_servicio.html'
    
#Categoria
class CategoriaList (ListView):
    model = Categoria
    template_name = 'templates/core/listar_categoria.html'
