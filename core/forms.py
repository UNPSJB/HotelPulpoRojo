from django import forms
from .models import Persona, Encargado, Pais, Provincia, Localidad, TipoHabitacion, Rol, Cliente, Vendedor, Servicio
from django.contrib.auth.models import User

#Formularios de personas
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

#Formulario de Cliente. Hereda de Persona.
class ClienteForm(PersonaForm):
    class Meta:
        model = Persona
        exclude = [
            'usuario'
        ]

#Formulario de Encargado. Hereda de Persona.
class EncargadoForm(PersonaForm):
    class Meta:
        model = Persona
        exclude = [
            'usuario'
        ]

#Formulario de Vendedor.
class VendedorForm(forms.ModelForm):
    #Definimos los campos a mostrar en el formulario
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'tipo_documento',
            'documento',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'tipo_documento': 'Tipo de Documento',
            'documento': 'Número de Documento',
            'usuario': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirme la contraseña'
        }
        
        
#Formulario para crear al vendedor
class CrearVendedorForm(VendedorForm):
    usuario = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    #Guardamos a la persona usando el método hacer_vendedor para asignarle el rol y el usuario de Django
    def save(self, commit=True):
        # localidad = LocalidadForm(self.cleaned_data).save(commit=commit)
        persona = super().save(commit=commit)
        return persona.hacer_vendedor(self.cleaned_data["usuario"], self.cleaned_data["email"], self.cleaned_data["password1"])

    #Validaciones para el usuario
    def clean_usuario(self):
        usuario = self.cleaned_data["usuario"]
        if len(usuario)<6:
            raise forms.ValidationError("La longitud mínima para un usuario es de 6 caracteres")
        if " " in usuario:
            raise forms.ValidationError("No seas animal, no pongas espacios")
        if User.objects.filter(username=usuario).exists():
            raise forms.ValidationError("El usuario ya existe")
        return usuario
    
    #Validación para el password
    def clean(self):
        data = super().clean()
        if data["password1"]!=data["password2"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return data

#Formulario para editar el Vendedor. Por el momento, es idéntico al crear.
class EditarVendedorForm(VendedorForm):
    pass

#Formulario del Administrador. 
class AdministradorForm(forms.ModelForm):
    #Definimos los campos a mostrar en el formulario
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'tipo_documento',
            'documento',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'tipo_documento': 'Tipo de Documento',
            'documento': 'Número de Documento',
            'usuario': 'Nombre de Usuario',
            'password1': 'Contraseña',
            'password2': 'Confirme la contraseña'
        }
        
#Formulario para crear al Administrador
class CrearAdministradorForm(AdministradorForm):
    usuario = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    #Guardamos a la persona usando el método hacer_administrador para crearle usuario de Django
    def save(self, commit=True):
        persona = super().save(commit=commit)
        return persona.hacer_administrador(self.cleaned_data["usuario"], self.cleaned_data["email"], self.cleaned_data["password1"])

    #Validaciones para el usuario
    def clean_usuario(self):
        usuario = self.cleaned_data["usuario"]
        if len(usuario)<6:
            raise forms.ValidationError("La longitud mínima para un usuario es de 6 caracteres")
        if " " in usuario:
            raise forms.ValidationError("No seas animal, no pongas espacios")
        if User.objects.filter(username=usuario).exists():
            raise forms.ValidationError("El usuario ya existe")
        return usuario

    #Validación para el password
    def clean(self):
        data = super().clean()
        if data["password1"]!=data["password2"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return data

#Formulario para editar el Administrador. Por el momento, es idéntico al crear.
class EditarAdministradorForm(AdministradorForm):
    pass


#Formularios de zona
class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

#Cosa rara: CrearVendedorForm.base_fields.update(LocalidadForm.base_fields)  Implicaría sobrecargar el save()

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'    

#formularios de servicio
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'    

class CrearServicioForm(ServicioForm):
    nombre = forms.CharField(widget=forms.TextInput)
    descripcion = forms.CharField(widget=forms.TextInput)
    
    def save(self, commit=True):
        servicio = ServicioForm(self.cleaned_data).save(commit=commit)

'''
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            'nombre',
            'descripcion',
        ]
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
        }
'''