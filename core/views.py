from django.shortcuts import render,redirect

# Create your views here.
from .models import Persona
from .forms import PersonaForm,ProvinciaForm,LocalidadForm,PaisForm

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
    return render(request,'iniciar_sesion.html')

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