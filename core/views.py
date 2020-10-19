from django.shortcuts import render,redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

# Create your views here.
from .models import Persona
from .forms import PersonaForm,ProvinciaForm,LocalidadForm,PaisForm

def index(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "index.html")
    # En otro caso redireccionamos al login
    return redirect('/iniciar_sesion')

def listarPersona(request):
    personas = Persona.objects.all() #select * from Persona
    contexto = { 
        'personas':personas
        }
    return render(request,'listar_persona.html',contexto)

def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form
            }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listar_persona')
    return render(request,'crear_persona.html',contexto)

def editarPersona(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance=persona)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST,instance=persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('listar_persona')
    return render(request,'crear_persona.html',contexto)

def eliminarPersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('listar_persona')

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
                return redirect('/listar_persona')

    # Si llegamos al final renderizamos el formulario
    return render(request, "iniciar_sesion.html", {'form': form})

    #return render(request,'iniciar_sesion.html')

def cerrarSesion(request):
    #Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


#Hay que investigar como hacer para que puedan aceptarse mas
#de un formualario en un vista
def crearZona(request):
    form1 = PaisForm()
    form2 = LocalidadForm()
    form3 = ProvinciaForm()
    contexto = {
        'PaisForm':form1
        }
    return render(request,'crear_zona.html',contexto)